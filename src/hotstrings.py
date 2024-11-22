import json
import logging
import sys
import time
from collections import deque
from pathlib import Path
import re

import keyboard
import mouse
import pyperclip
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QSystemTrayIcon, QMenu,
                             QAction, QInputDialog, QMessageBox)
from calc import Calc
from convert import convert
import bulk_functions as bulk
from unit_tests import unit_tests
from macro_settings import Macro_Settings


logging.basicConfig(
    filename='log.txt', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Hotstrings(QObject):
    macro_signal = pyqtSignal()
    edit_macro_signal = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.macro_signal.connect(self.spawn_macro_settings)
        self.edit_macro_signal.connect(self.spawn_macro_settings)
        self.app = QApplication([])
        self.restart = False
        # State flags
        self.paused = False
        self.debug_flag = False
        # Used to help gather input for bulk functions
        self.bulk = None
        self.calc = Calc(self)
        self.cwd = Path.cwd()
        self.settings_path = self.cwd / 'settings.json'
        if self.settings_path.exists():
            self.load_settings()
        else:
            self.endchar = '\\'
            self.user_macros = {}
            self.save_settings()
        self.last_output = ''
        self.load_hotstrings()
        self.callables = {
            'bb': bulk.blackboard_bold,
            'bold': bulk.bold,
            'boldcursive': bulk.boldcursive,
            'bolditalic': bulk.bolditalic,
            'braille': bulk.braille,
            'calc': self.calc.calc,
            'calculator': self.calc.calculator,
            '##': bulk.colors_to_hex,
            'convert': convert,
            'cursive': bulk.cursive,
            'delete macro': lambda user_input = None: bulk.delete_macro(self, user_input),
            'delete macros': lambda: bulk.delete_macro(self, 'all'),
            'edit macro': self.edit_macro,
            'flip': bulk.flip,
            'flipcase': bulk.flip_case,
            'funcs': lambda: self.calc.calc('funcs'),
            'functions': lambda: self.calc.calc('funcs'),
            'hearts': bulk.hearts,
            'hearts2': bulk.hearts2,
            '#': bulk.hex_to_colors,
            'hide': bulk.hide,
            'italic': bulk.italic,
            'lookalike': bulk.lookalike,
            'lower': bulk.lower,
            'lower2': bulk.lower2,
            'macros': self.macros,
            'mock': bulk.mock,
            'mock2': bulk.mock2,
            'mono': bulk.mono,
            'morse': bulk.morse,
            'morse2': bulk.morse2,
            'play': self.play,
            'python': bulk.python,
            'record': self.start_record,
            'recordk': lambda: self.start_record(record_mouse = False),
            'recordm': lambda: self.start_record(record_keyboard = False),
            'rot13': bulk.rot13,
            'rune': bulk.rune,
            'rune2': bulk.rune2,
            'smallcaps': bulk.smallcaps,
            'smallcaps2': bulk.smallcaps2,
            'solve': self.calc.solve,
            '__': bulk.subscript,
            '^^': bulk.superscript,
            'test': self.test_hotstrings,
            'unbraille': bulk.unbraille,
            'underline': bulk.underline,
            'unhide': bulk.unhide,
            'U+': bulk.unicode,
            'unmorse': bulk.unmorse,
            'unrune': bulk.unrune,
            'unrune2': bulk.unrune2,
            'vars': lambda: self.calc.calc('vars')
        }
        # Make sure the user_input deque is large enough to handle the largest valid hotstring
        # Make it double that length to account for things like user backspaces, arrow keys, etc
        maxlen = 0
        for key in self.Hotstrings | self.hotstrings | self.callables | self.user_macros:
            maxlen = max(maxlen, len(key))
        self.user_input = deque(maxlen = 2*maxlen)
        self.create_tray_icon()
        self.create_hooks()
    
    def backspace(self, n):
        """Sends n backspace presses"""
        for _ in range(n):
            keyboard.press_and_release('backspace')
    
    def change_endchar(self):
        """Changes the endchar"""
        text, ok = QInputDialog.getText(None, 'Change endchar', f'Enter the new endchar:')
        # For a reason I never discovered, this input dialog causes the self.app execution loop to end
        # So this self.restart flag tells it to start again in self.run()
        self.restart = True
        if ok and text:
            if len(text) == 1:
                self.endchar = text
                self.save_settings()
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Setting endchar failed')
                dlg.setText('Error: The endchar must be exactly 1 character. No changes made.')
                dlg.exec()
    
    def check_hotstrings(self, typed_string, testing = False):
        """Checks what the user typed to see if it contains a hotstring"""
        hs, rp = '', None
        # Check if they typed a case-sensitive hotstring
        for hotstring, replacement in self.Hotstrings.items():
            if typed_string.endswith(hotstring):
                if len(hotstring) > len(hs):
                    hs, rp = hotstring, replacement
        # Check if they typed a case-insensitive hotstring
        for hotstring, replacement in self.hotstrings.items():
            if typed_string.lower().endswith(hotstring.lower()):
                if len(hotstring) > len(hs):
                    hs, rp = hotstring, replacement
        # Check if they called a hotstring to a special function
        for hotstring, replacement in self.callables.items():
            if typed_string.lower().endswith(hotstring.lower()):
                if len(hotstring) > len(hs):
                    hs, rp = hotstring, replacement
        # Above loops never use 'break' after finding a match because we want to ensure we use the LONGEST matching hotstring
        # If the user types 'blueheart', for example, it should not match to just 'heart'
        if hs:
            # Found a match! Clear user_input
            self.user_input.clear()
            if testing:
                # User didn't type this, testing code did - return the output
                return rp
            # Backspace the typed hotstring, +1 for the endchar
            self.backspace(len(hs) + 1)
            if callable(rp):
                # It's a function, call it and gather its output
                output = rp()
                if isinstance(output, dict):
                    # If it returns a dict, it's a bulk function that needs more input to work
                    # Finish these universal parts of the dict
                    self.bulk = output
                    self.bulk['func'] = rp
                    self.bulk['start'] = time.time()
                    self.bulk['input'] = []
                elif isinstance(output, str):
                    # If it returns a string, no further input is needed - just write the output!
                    self.write(output)
            else:
                # It was a basic hotstring - write the output! 
                self.write(rp)
        else:
            if match := re.search(r'(-?[\d]*\.?[\d]*)([cCfF])$', typed_string):
                # User input ended in a celsius or fahrenheit temperature like "14.7f" - convert it to the other
                self.quickTemp(match)
    
    def clear_input(self):
        """Clears user_input and ends any bulk collection"""
        self.user_input.clear()
        self.bulk = None
    
    def create_hooks(self):
        """Removes any existing hooks, then creates all the usual ones"""
        mouse.unhook_all()
        # Clicking the mouse clears input - makes it impossible to determine what was actually typed
        mouse.on_click(self.clear_input)
        mouse.on_right_click(self.clear_input)
        keyboard.unhook_all()
        keyboard.on_press(self.handle_input_wrapper)
        keyboard.add_hotkey('win+z', self.toggle_pause)
        keyboard.add_hotkey('ctrl+v', self.pasted)
        for macro in self.user_macros.values():
            hotkey = macro['hotkey']
            events = macro['events']
            speed_factor = macro['speed_factor']
            repeat_count = macro['repeat_count']
            skip_paths = macro['skip_paths']
            keyboard.add_hotkey(hotkey, self.play, args = [hotkey, events, speed_factor, repeat_count, skip_paths])
    
    def create_tray_icon(self):
        """Creates the system tray icon and context menu"""
        # Defines self.normal_icon and self.paused_icon
        self.find_tray_icons()
        # Set the initial icon
        self.tray_icon = QSystemTrayIcon(QIcon(self.normal_icon))
        # Set hover text
        self.tray_icon.setToolTip('Hotstrings')
        # Create the context menu
        self.menu = QMenu()
        # Add Pause option to context menu
        self.pause_menu_item = QAction('Pause', self.app)
        self.pause_menu_item.triggered.connect(self.toggle_pause)
        self.menu.addAction(self.pause_menu_item)
        # Add Change endchar option to context menu
        endchar_change = QAction('Change endchar', self.app)
        endchar_change.triggered.connect(self.change_endchar)
        self.menu.addAction(endchar_change)
        # Add Log Current State to context menu
        self.debug_menu_item = QAction('Enable Debug Logging', self.app)
        self.debug_menu_item.triggered.connect(self.debug)
        self.menu.addAction(self.debug_menu_item)
        # Add Exit option to context menu
        exit_action = QAction('Exit', self.app)
        exit_action.triggered.connect(self.exit_app)
        self.menu.addAction(exit_action)
        # Add the context menu to the system tray icon
        self.tray_icon.setContextMenu(self.menu)
        # Add event trigger for when icon is clicked
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        # Display the tray icon
        self.tray_icon.show()
    
    def debug(self):
        """Toggles the debug state on and off"""
        if self.debug_flag:
            # Turn debug logging off
            self.debug_flag = False
            self.debug_menu_item.setText('Enable Debug Logging')
        else:
            # Turn debug logging on
            self.debug_flag = True
            self.debug_menu_item.setText('Disable Debug Logging')
    
    def edit_macro(self, user_input = None):
        """Opens the Macro Settings window to edit an existing macro"""
        if not user_input:
            return {'func': self.edit_macro,
                    'max': 500,
                    'time': 90}
        if user_input in self.user_macros:
            # User provided the (typed) hotkey to activate a macro, edit that one
            macro = self.user_macros[user_input]
            self.edit_macro_signal.emit(macro)
        elif user_input.isdigit() and 1 <= (user_int := int(user_input)) <= len(self.user_macros):
            # See if the user entered a number that corresponds to a macro - use 'macros' hotstring to see list
            macro_to_edit = list(self.user_macros.keys())[user_int - 1]
            macro = self.user_macros[macro_to_edit]
            self.edit_macro_signal.emit(macro)
        else:
            return 'Invalid macro'
    
    def exit_app(self):
        """Quits the app"""
        keyboard.unhook_all()
        mouse.unhook_all()
        self.tray_icon.hide()
        QApplication.quit()
        exit()
    
    def find_tray_icons(self):
        """Locates .ico files to use for system tray icons, or uses default images if none are present"""
        # Define the system tray icons to be used normally, and when paused
        # Prefer local icon files if present
        normal = self.cwd / 'normal.ico'
        self.normal_icon = str(normal) if normal.exists() else False
        paused = self.cwd / 'paused.ico'
        self.paused_icon = str(paused) if paused.exists() else False
        # If no local files, try in /assets/images
        if not self.normal_icon:
            normal = self.cwd.parent / 'assets/images/normal.ico'
            self.normal_icon = str(normal) if normal.exists() else False
        if not self.paused_icon:
            paused = self.cwd.parent / 'assets/images/paused.ico'
            self.paused_icon = str(paused) if paused.exists() else False
        # If running from .exe, pyinstaller makes temp directory here, which will contain icons
        if not self.normal_icon and (meipass := getattr(sys, '_MEIPASS', False)):
            normal = Path(meipass) / 'normal.ico'
            self.normal_icon = str(normal) if normal.exists() else False
        if not self.paused_icon and (meipass := getattr(sys, '_MEIPASS', False)):
            paused = Path(meipass) / 'paused.ico'
            self.paused_icon = str(paused) if paused.exists() else False
        # If all else fails just use a default icon for both
        if not self.normal_icon:
            self.normal_icon = QIcon(QApplication.style().standardIcon(QApplication.style().SP_ComputerIcon))
        if not self.paused_icon:
            self.paused_icon = QIcon(QApplication.style().standardIcon(QApplication.style().SP_ComputerIcon))
    
    def get_typed_string(self, user_input, forgiving = False):
        """Parses user_input to determine what the user likely actually typed"""
        typed_string = []
        # insert_pos is only necessary to support letting the user use the left and right arrow keys
        insert_pos = 0
        if len(user_input) == 0:
            return ''
        while user_input[0].name in ['left', 'right', 'backspace', 'up', 'down']:
            # None of these events mess up the string logic when at the start of a string
            # But removing them now allows the logic below to be simpler
            del user_input[0]
            if len(user_input) == 0:
                return ''
        for i, event in enumerate(user_input):
            if not isinstance(event, keyboard.KeyboardEvent):
                continue
            if event.name == 'v':
                if i > 0 and user_input[i-1].name == 'paste':
                    # User hit ctrl+v to paste, and we handled this in the previous event - skip
                    continue
                typed_string.insert(insert_pos, event.name)
                insert_pos += 1
            elif len(event.name) == 1:
                # User typed a regular character, insert it into their typed string
                typed_string.insert(insert_pos, event.name)
                insert_pos += 1
            elif event.name == 'space':
                typed_string.insert(insert_pos, ' ')
                insert_pos += 1
            elif event.name == 'left':
                # Pressed the left key, move the insert position
                insert_pos -= 1
                if insert_pos < 0:
                    # If they tried to move left of the first position, we have no
                    # way of knowing what their input looks like - so just give up
                    # Or if we're feeling forgiven, start over from here
                    if not forgiving:
                        return None
                    typed_string = []
                    insert_pos = 0
            elif event.name == 'right':
                insert_pos += 1
                if insert_pos > len(typed_string):
                    # If they tried to move right of the rightmost position, we have no
                    # way of knowing what their input looks like - so just give up
                    # Or if we're feeling forgiven, start over from here
                    if not forgiving:
                        return None
                    typed_string = []
                    insert_pos = 0
            elif event.name in ['up', 'down']:
                # Both of these keys make it impossible to accurately
                # determine what the user input looks like, give up
                # Or if we're feeling forgiven, start over from here
                if not forgiving:
                    return None
                typed_string = []
                insert_pos = 0
            elif event.name == 'backspace':
                if insert_pos >= 1:
                    del typed_string[insert_pos - 1]
                    insert_pos -= 1
            elif event.name == 'enter':
                typed_string.insert(insert_pos, '\n')
                insert_pos += 1
            elif event.name == 'tab':
                typed_string.insert(insert_pos, '\t')
                insert_pos += 1
            elif event.name == 'paste':
                typed_string.insert(insert_pos, event.device)
                insert_pos += 1
        return ''.join(typed_string[:insert_pos])
    
    def handle_input(self, event):
        """Handles all input"""
        if self.paused:
            # Do nothing if we're paused
            return
        if event.scan_code == 99:
            # Function key, event.name == None by default, causes issues
            event.name = 'fn'
        if event.name == self.endchar:
            # User typed the endchar!
            if self.bulk:
                # We were already gathering input for a bulk function - time to process that input
                # Combine everything typed into one string
                text = self.get_typed_string(self.bulk['input'])
                self.bulk['input'] = []
                if text is None:
                    # User input wasn't possible to unambiguously parse
                    self.bulk = None
                    return
                # Keep track of how much to backspace (+1 for endchar)
                backspace_count = len(text) + 1
                # Special built-in variable: _ in user input gets changed to the last output
                # calculator stuff handles this in a custom way
                if getattr(self.bulk['func'], '__self__', None) is not self.calc:
                    text = text.replace('_', self.last_output)
                if not text and self.bulk['func'] != self.calc.calculator:
                    # If nothing was typed, pull from the clipboard
                    # Don't do that in self.calc.calculator because entering no input is how you quit
                    text = pyperclip.paste()
                    if len(text) > self.bulk['max']:
                        # Give up and do nothing if there's too much text in the clipboard
                        self.bulk = None
                        return
                try:
                    # Send the input to the function
                    output = self.bulk['func'](text)
                    if self.bulk['func'] == self.calc.calculator and output == 'end_calculator':
                        # Calculator sends that output when it's time to quit
                        # Remove 'func' so below code will properly exit
                        self.bulk['func'] = None
                        output = ''
                    # Backspace all the user input
                    self.backspace(backspace_count)
                    # Write the function output
                    self.write(output)
                except:
                    error_message = ['Unhandled exception when processing bulk input']
                    error_message.append(f'{self.bulk["func"].__name__ = }')
                    error_message.append(f'{self.bulk = }')
                    error_message.append(f'{text = }')
                    error_message.append('')
                    logging.exception('\n'.join(error_message))
                finally:
                    # Stop bulk collection
                    if self.bulk['func'] != self.calc.calculator:
                        self.bulk = None
                    else:
                        self.bulk['input'] = []
            else:
                # Not in a bulk function, so check for a normal hotstring
                # Combine everything typed into one string
                text = self.get_typed_string(self.user_input, forgiving = True)
                self.user_input.append(event)
                try:
                    # Send it off to check if it contains a valid hotstring
                    self.check_hotstrings(text)
                except Exception as e:
                    error_message = ['Unhandled exception in check_hotstrings']
                    error_message.append(f'{text = }')
                    error_message.append('')
                    logging.exception('\n'.join(error_message))
        elif self.bulk:
            # We're doing input collection for a bulk function!
            self.bulk['input'].append(event)
            if len(self.bulk['input']) > self.bulk['max']:
                # Typed too much
                self.bulk = None
                return
            if time.time() - self.bulk['start'] > self.bulk['time']:
                # Took too long
                self.bulk = None
                return
        else:
            # Regular input, just toss it in the queue
            self.user_input.append(event)
    
    def handle_input_wrapper(self, event):
        """Calls handle_input, logs current state in event of errors"""
        try:
            if self.debug_flag: self.log_state()
            self.handle_input(event)
            if self.debug_flag: self.log_state()
        except Exception:
            error_message = ['Unhandled exception in handle_input']
            error_message.append(f'{self.bulk = }')
            if self.bulk:
                error_message.append(f'{self.bulk["func"].__name__ = }')
                error_message.append(f'{self.bulk["input"] = }')
                error_message.append(f'{self.get_typed_string(self.bulk["input"]) = }')
                error_message.append(f'{self.get_typed_string(self.bulk["input"], forgiving = True) = }')
            error_message.append(f'{self.user_input = }')
            error_message.append(f'{self.get_typed_string(self.user_input) = }')
            error_message.append(f'{self.get_typed_string(self.user_input, forgiving = True) = }')
            error_message.append('')
            logging.exception('\n'.join(error_message))
    
    def load_hotstrings(self):
        """Reads the hotstrings.json file and loads it into memory"""
        # Prefer a hotstrings.json in the cwd if it exists
        hotstrings_path = self.cwd / 'hotstrings.json'
        if not hotstrings_path.exists():
            # Otherwise check the MEIPASS directory, which the pyinstaller .exe creates
            if meipass := getattr(sys, '_MEIPASS', False):
                hotstrings_path = Path(meipass) / 'hotstrings.json'
            if not hotstrings_path.exists():
                raise Exception('hotstrings.json file not present!')
        with open(hotstrings_path, 'r', encoding='utf-8') as f:
            all_hotstrings = f.read()
        # Remove comments from the hotstrings, as they aren't actually allowed
        all_hotstrings = re.sub(r'//.*', '', all_hotstrings)
        all_hotstrings = json.loads(all_hotstrings)
        # Case-sensitive Hotstrings
        self.Hotstrings = all_hotstrings['Hotstrings']
        # Case-insensitive hotstrings
        self.hotstrings = all_hotstrings['hotstrings']
    
    def load_settings(self):
        """Loads settings from file"""
        with open(self.settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
        self.endchar = settings['endchar']
        if 'user_macros' in settings:
            self.user_macros = settings['user_macros']
        else:
            self.user_macros = {}
        if 'user_vars' in settings:
            user_vars = settings['user_vars']
            for key, value in user_vars.items():
                if isinstance(value, str):
                    user_vars[key] = complex(value)
            self.calc.user_vars = user_vars
        if 'user_funcs_raw' in settings:
            self.calc.user_funcs_raw = settings['user_funcs_raw']
        self.calc.update_user_funcs()
    
    def log_state(self):
        """Adds current values various variables to the log file"""
        log_message = ['LOGGING CURRENT STATE']
        log_message.append(f'{self.endchar = }')
        log_message.append(f'{self.restart = }')
        log_message.append(f'{self.paused = }')
        log_message.append(f'{self.last_output = }')
        log_message.append(f'{self.bulk = }')
        log_message.append(f'{self.user_input = }')
        log_message.append(f'{self.get_typed_string(self.user_input) = }')
        log_message.append(f'{self.get_typed_string(self.user_input, forgiving = True) = }')
        if self.bulk:
            log_message.append(f'\t{self.bulk = }')
            log_message.append(f'\t{self.bulk["func"].__name__ = }')
            log_message.append(f'\t{self.bulk["input"] = }')
            log_message.append(f'\t{self.get_typed_string(self.bulk["input"]) = }')
            log_message.append(f'\t{self.get_typed_string(self.bulk["input"], forgiving = True) = }')
        else:
            log_message.append(f'{self.bulk = }')
        log_message.append('END OF CURRENT STATE')
        log_message.append('')
        logging.info('\n'.join(log_message))
    
    def macros(self):
        """Outputs a list of the user-defined macros"""
        output = []
        for i, macro in enumerate(self.user_macros, start = 1):
            output.append(f'{i}: {macro}')
        if output:
            return 'User macros:\n' + '\n'.join(output)
        else:
            return 'No user macros defined.'
    
    def on_tray_icon_activated(self, reason):
        """Pauses the app when system tray icon is double clicked"""
        # This function basically just makes sure it takes a double click, not a single click, to do this
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_pause()
    
    def pasted(self):
        """Detects paste events, adds them to bulk input"""
        # Paste events are only relevant to bulk input
        if self.bulk:
            # Custom way I store paste events - clipboard data in the device parameter
            event = keyboard.KeyboardEvent('down', 29, 'paste', device = pyperclip.paste())
            self.bulk['input'].append(event)
    
    def play(self, hotkey, events, speed_factor, repeat_count, skip_paths):
        """Plays back a macro"""
        # If any modifier keys are currently pressed, this unpresses them
        state = keyboard.stash_state()
        # Remove all hooks for playback
        keyboard.unhook_all()
        mouse.unhook_all()
        # Creates a list of all keys in the hotkey that activates this macro
        hotkey_keys = hotkey.split('+')
        while True:
            # When the macro is first started, the user is usually still holding down the hotkey
            # This loop waits until they've released every key in the hotkey before starting the macro
            breakout = True
            for key in hotkey_keys:
                if keyboard.is_pressed(key):
                    breakout = False
            if breakout:
                break
            time.sleep(0.01)
        if skip_paths:
            # We're skipping all mouse paths, but we still want to keep MouseMove events that precede
            # MouseButton events, so the click happens in the correct location
            # Reverse the events, iterate through it - save every MouseMove event that's the first one
            # to appear after a MouseButton event, mark all the rest for deletion - then delete them
            # and un-reverse the events
            events = events[::-1]
            save_next = False
            to_delete = []
            for i, event in enumerate(events):
                if event['event'] == 'button':
                    # Encountered a button event, so save the next move event
                    save_next = True
                elif event['event'] == 'move':
                    if save_next:
                        # This is the first move event after a button event - don't delete it
                        save_next = False
                    else:
                        # This move event just helps define a mouse path, delete it
                        to_delete.append(i)
            for i in to_delete[::-1]:
                del events[i]
            events = events[::-1]
        while repeat_count > 0:
            for i, event in enumerate(events):
                if keyboard.is_pressed(hotkey):
                    # If the user is pressing the hotkey, wait for them to let go, then end the macro and rebuild hooks
                    while keyboard.is_pressed(hotkey):
                        time.sleep(0.01)
                    keyboard.restore_modifiers(state)
                    return self.create_hooks()
                # Timing loop:
                if i > 0:
                    # First event always starts immediately
                    # Wait the amount of time between this event and the previous one, divided by the speed factor
                    go_time = time.time() + (event['time'] - events[i-1]['time']) / speed_factor
                    while (current_time := time.time()) < go_time:
                        if keyboard.is_pressed(hotkey):
                            # If the macro hotkey is pressed, end the macro and rebuildhooks
                            while keyboard.is_pressed(hotkey):
                                time.sleep(0.01)
                            keyboard.restore_modifiers(state)
                            return self.create_hooks()
                        # Sleep in .01 second increments or less, until enough time has elapsed
                        time.sleep(min(0.01, go_time - current_time))
                # Processes each kind of event that can be encountered, and carries it out
                if event['event'] == 'button': # Mouse was clicked
                    mouse.release(event['name']) if event['type'] == mouse.UP else mouse.press(event['name'])
                elif event['event'] == 'move': # Mouse was moved
                    mouse.move(event['x'], event['y'])
                elif event['event'] == 'wheel': # Mouse wheel was scrolled
                    mouse.wheel(event['delta'])
                elif event['event'] == 'key': # Keyboard key was pressed
                    key = event['scan_code'] or event['name']
                    keyboard.press(key) if event['type'] == keyboard.KEY_DOWN else keyboard.release(key)
            repeat_count -= 1
        # All done, rebuild hooks
        keyboard.restore_modifiers(state)
        return self.create_hooks()
    
    def quickTemp(self, match):
        """Converts matched temperature between fahrenheit and celsius"""
        # match already contains a temperature, with group 1 being a number and group 2 being f or c
        try:
            temperature = float(match.group(1))
        except:
            # Regex used to identify numbers here isn't foolproof ¯\_(ツ)_/¯
            return
        unit = match.group(2)
        backspace_count = len(match.group(1)) + len(match.group(2)) + 1
        if unit.lower() == 'f':
            # Convert from fahrenheit to celsius
            temperature = (temperature - 32)*5/9
            temperature = round(temperature, 2)
            output = f'{temperature}℃'
        else:
            # Convert from celsius to fahrenheit
            temperature = 1.8*temperature + 32
            temperature = round(temperature, 2)
            output = f'{temperature}℉'
        self.backspace(backspace_count)
        self.write(output)
    
    def record(self, event, record_keyboard, record_mouse):
        """Records keyboard and mouse events to create a macro"""
        if event.name == self.endchar and event.event_type == keyboard.KEY_DOWN:
            # Endchar is encountered, end collection
            self.create_hooks()
            # It will usually catch the keyboard up event for the endchar that activated recording
            # So find and remove it
            for i, event in enumerate(self.events):
                if isinstance(event, keyboard.KeyboardEvent):
                    if event.name == self.endchar and event.event_type == keyboard.KEY_UP:
                        del self.events[i]
                    # If present it'll always be the first KeyboardEvent, so break if we find one and it isn't
                    break
            # Make self.events json-serializable
            self.serialize_events()
            if record_mouse:
                # The first event in self.events will always be a MouseMove to the mouse's current position
                # This event is created the moment the recording starts - below if statement will update its
                # time attribute to match the first real user input
                if len(self.events) > 1:
                    self.events[0]['time'] = self.events[1]['time']
                # The initial MouseMove event, which we created, is only needed if a button event
                # is encountered before the first move event - this for loop checks for that, and
                # either keeps or deletes the first event as appropriate
                for event in self.events[1:]:
                    if event['event'] == 'move':
                        del self.events[0]
                        break
                    elif event['event'] == 'button':
                        break
                else:
                    # We can also delete it if there are simply no other mouse events at all
                    del self.events[0]
            # Remove the endchar
            keyboard.press_and_release('backspace')
            # Spawn the macro settings window
            self.macro_signal.emit()
        else:
            self.events.append(event)
    
    def run(self):
        """Begins the main execution loop"""
        self.app.exec_()
        # There are some known events which stop the execution loop consistently when we don't actually want to
        # They set this flag so we can avoid ending the execution loop
        if self.restart:
            self.restart = False
            self.run()
    
    def save_settings(self):
        """Saves current settings to file"""
        settings = {}
        settings['endchar'] = self.endchar
        settings['user_vars'] = self.calc.user_vars
        settings['user_funcs_raw'] = self.calc.user_funcs_raw
        for key, value in settings['user_vars'].items():
            if isinstance(value, complex):
                settings['user_vars'][key] = str(value)
        settings['user_macros'] = self.user_macros
        with open(self.settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
    
    def serialize_events(self):
        """Converts KeyboardEvent and similar events into json-serializable dicts, so they can be saved to file"""
        first_time = self.events[0].time
        for i, event in enumerate(self.events):
            if isinstance(event, mouse.ButtonEvent):
                event = {'event': 'button',
                         'name': event.button,
                         'type': event.event_type,
                         'time': event.time - first_time}
            elif isinstance(event, mouse.MoveEvent):
                event = {'event': 'move',
                         'x': event.x,
                         'y': event.y,
                         'time': event.time - first_time}
            elif isinstance(event, mouse.WheelEvent):
                event = {'event': 'wheel',
                         'delta': event.delta,
                         'time': event.time - first_time}
            elif isinstance(event, keyboard.KeyboardEvent):
                event = {'event': 'key',
                         'scan_code': event.scan_code,
                         'name': event.name,
                         'type': event.event_type,
                         'time': event.time - first_time}
            else:
                raise TypeError(f'Unknown event type: {event}')
            self.events[i] = event
    
    def spawn_macro_settings(self, macro = None):
        """Opens the window to configure and save macros"""
        try:
            # For an unknown reason the program always exits after doing this, so.. this flag tells it to immediately restart
            self.restart = True
            if macro:
                # User is editing an existing macro
                self.settings = Macro_Settings(self, None, macro)
            else:
                # A new macro has been recorded, and is currently in self.events
                self.settings = Macro_Settings(self, self.events, macro)
                del self.events
            self.settings.show()
        except Exception as e:
            logging.exception('Unhandled exception in spawn_macro_settings\n')
    
    def start_record(self, record_keyboard = True, record_mouse = True):
        """Sets up to record keyboard and mouse input for macro creation"""
        # Keyboard and mouse events will be stored in self.events
        self.events = []
        # Remove all hooks so we can redirect them to the recorder
        keyboard.unhook_all()
        mouse.unhook_all()
        # Keyboard data is always sent to the recorder, even if we aren't saving it, for endchar detection
        keyboard.hook(lambda event: self.record(event, record_keyboard, record_mouse))
        # Only bother sending mouse data to the recorder if we're actually recording it
        if record_mouse:
            # Create a MoveEvent at the mouse's initial position as the first event, as this is not saved otherwise
            # Ensures mouse begins at the correct location, only relevant if a ButtonEvent occurs before a MoveEvent
            mouse_pos = mouse.get_position()
            mouse_pos = mouse.MoveEvent(mouse_pos[0], mouse_pos[1], time.time())
            self.events.append(mouse_pos)
            mouse.hook(self.events.append)
    
    def test_hotstrings(self):
        """Tests every hotstring to verify it gives the correct output, and runs the unit tests"""
        passes = 0
        fails = 0
        # Check case-sensitive hotstrings, case-insensitive hotstrings, and callable hotstrings
        for hs_dict in [self.Hotstrings, self.hotstrings, self.callables]:
            # Check each hotstring
            for hs, rp in hs_dict.items():
                # And see if its actual output matches its expected output
                output = self.check_hotstrings(hs, testing = True)
                if output == rp:
                    passes += 1
                else:
                    fails += 1
                    self.write(f"Fail: '{hs}' yielded '{output}' instead of '{rp}'\n")
        self.write(f'{passes = }, {fails = }\n')
        # After, run the unit tests
        return unit_tests()
    
    def toggle_pause(self):
        """Toggles the current pause state and system tray icon"""
        self.paused = not self.paused
        if self.paused:
            self.tray_icon.setToolTip('Hotstrings - PAUSED')
            self.pause_menu_item.setText('Unpause')
            self.tray_icon.setIcon(QIcon(self.paused_icon))
        else:
            self.tray_icon.setToolTip('Hotstrings')
            self.pause_menu_item.setText('Pause')
            self.tray_icon.setIcon(QIcon(self.normal_icon))
    
    def write(self, text):
        """Writes the provided text"""
        if text:
            while '\n' in text:
                # It works without doing this, but it works as if just pressing 'enter'
                # In chat programs like discord this automatically sends messages, which is annoying
                # So this enters linebreaks as shift+enter instead, to avoid that
                index = text.index('\n')
                keyboard.write(text[:index])
                keyboard.press_and_release('shift+enter')
                text = text[index + 1:]
            keyboard.write(text)
            # Save the last output, which is used to define the special '_' variable
            self.last_output = text

def main():
    app = Hotstrings()
    app.run()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        logging.exception('Unhandled exception in main\n')
