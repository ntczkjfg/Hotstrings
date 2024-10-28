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
    spawn_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.spawn_signal.connect(self.spawn_window)
        self.app = QApplication([])
        self.restart = False
        # Track Paused state
        self.paused = False
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
            'flip': bulk.flip,
            'funcs': lambda: self.calc.calc('funcs'),
            'functions': lambda: self.calc.calc('funcs'),
            'hearts': bulk.hearts,
            'hearts2': bulk.hearts2,
            '#': bulk.hex_to_colors,
            'hide': bulk.hide,
            'italic': bulk.italic,
            'lookalike': bulk.lookalike,
            'macros': self.macros,
            'mock': bulk.mock,
            'mock2': bulk.mock2,
            'mono': bulk.mono,
            'morse': bulk.morse,
            'morse2': bulk.morse2,
            'play': self.play,
            'python': bulk.python,
            'record': self.record,
            'recordk': lambda: self.record(record_mouse = False),
            'recordm': lambda: self.record(record_keyboard = False),
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
            'unittest': unit_tests,
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
    
    def macros(self):
        output = []
        for i, macro in enumerate(self.user_macros, start = 1):
            output.append(f'{i}: {macro}')
        if output:
            output = 'User macros:\n' + '\n'.join(output)
        else:
            output = 'No user macros defined.'
        self.write(output)
    
    def spawn_window(self):
        self.settings = Macro_Settings(self, self.events)
        self.settings.show()
        del self.events
    
    def serialize_events(self):
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
    
    def record(self, event = None, record_keyboard = True, record_mouse = True):
        if event:
            if event.name == self.endchar and event.event_type == keyboard.KEY_DOWN:
                self.create_hooks()
                # It will usually catch the keyboard up event for the endchar that activated recording
                # So find and remove it
                for i, event in enumerate(self.events):
                    if isinstance(event, keyboard.KeyboardEvent):
                        if event.name == self.endchar and event.event_type == keyboard.KEY_UP:
                            del self.events[i]
                        break
                # Make self.events json-serializable
                self.serialize_events()
                # Remove the endchar
                keyboard.press_and_release('backspace')
                self.spawn_signal.emit()
                self.restart = True
            else:
                self.events.append(event)
        else:
            self.events = []
            keyboard.unhook_all()
            mouse.unhook_all()
            keyboard.hook(lambda event: self.record(event, record_keyboard, record_mouse))
            if record_mouse:
                mouse.hook(self.events.append)

    def play(self, hotkey, events, speed_factor, repeat_count):
        state = keyboard.stash_state()
        keyboard.unhook_all()
        keys = hotkey.split('+')
        while True:
            breakout = True
            for key in keys:
                if keyboard.is_pressed(key):
                    breakout = False
            if breakout:
                break
            time.sleep(0.01)
        while repeat_count > 0:
            last_time = None
            for event in events:
                if keyboard.is_pressed(hotkey):
                    while keyboard.is_pressed(hotkey):
                        time.sleep(0.01)
                    keyboard.restore_modifiers(state)
                    return self.create_hooks()
                if speed_factor and last_time:
                    go_time = time.time() + (event['time'] - last_time) / speed_factor
                    while (current_time := time.time()) < go_time:
                        if keyboard.is_pressed(hotkey):
                            while keyboard.is_pressed(hotkey):
                                time.sleep(0.01)
                            keyboard.restore_modifiers(state)
                            return self.create_hooks()
                        time.sleep(min(0.01, go_time - current_time))
                last_time = event['time']
                
                if event['event'] == 'button':
                    mouse.release(event['name']) if event['type'] == mouse.UP else mouse.press(event['name'])
                elif event['event'] == 'move':
                    mouse.move(event['x'], event['y'])
                elif event['event'] == 'wheel':
                    mouse.wheel(event['delta'])
                elif event['event'] == 'key':
                    key = event['scan_code'] or event['name']
                    keyboard.press(key) if event['type'] == keyboard.KEY_DOWN else keyboard.release(key)
            repeat_count -= 1
        keyboard.restore_modifiers(state)
        return self.create_hooks()
    
    def create_hooks(self):
        mouse.unhook_all()
        keyboard.unhook_all()
        keyboard.on_press(self.gather_input_1)
        keyboard.add_hotkey('win+z', self.toggle_pause)
        keyboard.add_hotkey('ctrl+v', self.pasted)
        for macro in self.user_macros.values():
            hotkey = macro['hotkey']
            events = macro['events']
            speed_factor = macro['speed_factor']
            repeat_count = macro['repeat_count']
            keyboard.add_hotkey(hotkey, self.play, args = [hotkey, events, speed_factor, repeat_count])
    
    def load_hotstrings(self):
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
    
    def save_settings(self):
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
    
    def create_tray_icon(self):
        """Creates the system tray icon and context menu"""
        # Define the icons to be used normally, and when paused
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
        
        # Set the initial icon
        self.tray_icon = QSystemTrayIcon(QIcon(self.normal_icon))
        
        # Set hover text
        self.tray_icon.setToolTip("Hotstrings")
        
        # Create the context menu
        self.menu = QMenu()
        # Add Pause option to context menu
        self.pause_action = QAction("Pause", self.app)
        self.pause_action.triggered.connect(self.toggle_pause)
        self.menu.addAction(self.pause_action)
        # Add Change endchar option to context menu
        endchar_change = QAction('Change endchar', self.app)
        endchar_change.triggered.connect(self.change_endchar)
        self.menu.addAction(endchar_change)
        # Add Exit option to context menu
        exit_action = QAction("Exit", self.app)
        exit_action.triggered.connect(self.exit_app)
        self.menu.addAction(exit_action)
        # Add the context menu to the system tray icon
        self.tray_icon.setContextMenu(self.menu)
        
        # Add event trigger for when icon is clicked
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        
        # Display the tray icon
        self.tray_icon.show()

    def change_endchar(self):
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
    
    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_pause()
    
    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.tray_icon.setToolTip("Hotstrings - PAUSED")
            self.pause_action.setText("Unpause")
            self.tray_icon.setIcon(QIcon(self.paused_icon))
        else:
            self.tray_icon.setToolTip("Hotstrings")
            self.pause_action.setText("Pause")
            self.tray_icon.setIcon(QIcon(self.normal_icon))
    
    def exit_app(self):
        self.tray_icon.hide()
        QApplication.quit()
        exit()
    
    def run(self):
        self.app.exec_()
        if self.restart:
            self.restart = False
            self.run()

    def get_typed_string(self, user_input):
        typed_string = []
        insert_pos = 0
        for i, event in enumerate(user_input):
            if not isinstance(event, keyboard.KeyboardEvent):
                continue
            if event.name == 'v':
                if i > 0 and user_input[i-1].name == 'paste':
                    continue
                typed_string.insert(insert_pos, event.name)
                insert_pos += 1
            elif len(event.name) == 1:
                typed_string.insert(insert_pos, event.name)
                insert_pos += 1
            elif event.name == 'space':
                typed_string.insert(insert_pos, ' ')
                insert_pos += 1
            elif event.name == 'left':
                insert_pos -= 1
                if insert_pos < 0:
                    insert_pos = 0
            elif event.name == 'right':
                insert_pos += 1
                if insert_pos > len(typed_string):
                    insert_pos = len(typed_string)
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
        return ''.join(typed_string)
    
    def gather_input_1(self, event):
        try:
            self.gather_input(event)
        except Exception:
            error_message = ['Unhandled exception in gather_input']
            if self.bulk:
                error_message.append(f'{self.bulk = }')
                error_message.append(f'{self.bulk["func"].__name__ = }')
                error_message.append(f'{self.bulk["input"] = }')
                error_message.append(f'{self.get_typed_string(self.bulk["input"]) = }')
            error_message.append(f'{self.user_input = }')
            error_message.append(f'{self.get_typed_string(self.user_input) = }')
            logging.exception('\n'.join(error_message))
    
    # Handles all input
    def gather_input(self, event):
        if self.paused:
            # Do nothing if we're paused
            return
        if event.name == self.endchar:
            # User typed the endchar!
            if self.bulk:
                # We were already gathering input for a bulk function - time to process that input
                # Combine everything typed into one string
                text = self.get_typed_string(self.bulk['input'])
                # Keep track of how much to backspace (+1 for endchar)
                backspace_count = len(text) + 1
                # Special built-in variable: _ in user input gets changed to the last output
                # calculator stuff handles this in a custom way
                if getattr(self.bulk['func'], '__self__', None) is not self.calc:
                    text = text.replace('_', self.last_output)
                if not text and self.bulk['func'] is not self.calc.calculator:
                    # If nothing was typed, pull from the clipboard
                    text = pyperclip.paste()
                    if len(text) > self.bulk['max']:
                        # Give up and do nothing if there's too much text in the clipboard
                        self.bulk = None
                        return
                try:
                    # Send the input to the function
                    output = self.bulk['func'](text)
                    if self.bulk['func'] is self.calc.calculator and output == 'end_calculator':
                        self.bulk['func'] = None
                        output = ''
                    # Backspace all the user input
                    for _ in range(backspace_count):
                        keyboard.press_and_release('backspace')
                    # Write the function output
                    self.write(output)
                except:
                    error_message = ['Unhandled exception when processing bulk input']
                    error_message.append(f'{self.bulk["func"].__name__ = }')
                    error_message.append(f'{text = }')
                    logging.exception('\n'.join(error_message))
                finally:
                    # Stop bulk collection
                    if self.bulk['func'] is not self.calc.calculator:
                        self.bulk = None
                    else:
                        self.bulk['input'] = []
                return
            else:
                # Not in a bulk function, so check for a normal hotstring
                # Combine everything typed into one string
                text = self.get_typed_string(self.user_input)
                try:
                    # Send it off to check if it contains a valid hotstring
                    self.check_hotstrings(text)
                except Exception as e:
                    error_message = ['Unhandled exception in check_hotstrings']
                    error_message.append(f'{text = }')
                    logging.exception('\n'.join(error_message))
                finally:
                    # Ensure user_input gets cleared, so further endchar presses don't activate the same one
                    self.user_input.clear()
        elif self.bulk:
            # We're doing input collection for a bulk function!
            self.bulk['input'].append(event)
            if len(self.bulk['input']) > self.bulk['max']:
                self.bulk = None
                return
            if time.time() - self.bulk['start'] > self.bulk['time']:
                self.bulk = None
                return
        else:
            # Regular input, just toss it in the queue
            self.user_input.append(event)

    def test_hotstrings(self):
        passes = 0
        fails = 0
        for hs_dict in [self.Hotstrings, self.hotstrings, self.callables]:
            for hs, rp in hs_dict.items():
                output = self.check_hotstrings(hs, testing = True)
                if output == rp:
                    passes += 1
                else:
                    fails += 1
                    self.write(f"Fail: '{hs}' yielded '{output}' instead of '{rp}'\n")
        self.write(f'{passes = }, {fails = }\n')
        return unit_tests()
    
    # The user pressed the endchar, and we weren't gathering input for a bulk function!
    def check_hotstrings(self, typed_string, testing = False):
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
            if testing:
                return rp
            # We found a match!
            for _ in range(len(hs) + 1):
                # Backspace the typed hotstring
                keyboard.press_and_release('backspace')
            if callable(rp):
                # It's a function - call it, and gather its output
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
    
    def pasted(self):
        # Custom way I store paste events - clipboard data in the device parameter
        event = keyboard.KeyboardEvent('down', 29, 'paste', device = pyperclip.paste())
        if self.bulk:
            self.bulk['input'].append(event)
        else:
            self.user_input.append(event)
    
    # Write the provided text
    def write(self, text):
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
        logging.exception('Unhandled exception in main')
