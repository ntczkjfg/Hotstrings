import json
import logging
import sys
import time
from collections import deque
from pathlib import Path
import re
import subprocess
import traceback
import platform

linux = platform.system() == 'Linux'
if linux:
    wayland = 'wayland' in subprocess.run(['ps', '-e', '-o', 'comm'], stdout=subprocess.PIPE).stdout.decode('utf-8').lower()
else:
    wayland = False
if wayland:
    from evdev import UInput, ecodes, InputDevice
    from evput import keyboard
if not wayland:
    import pyperclip
    from pynput import keyboard, mouse

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (QApplication, QSystemTrayIcon, QMenu,
                             QInputDialog, QMessageBox)
from calc import Calc
from convert import convert
import bulk_functions as bulk
from unit_tests import unit_tests
from macro_settings import Macro_Settings

logging.basicConfig(
    filename='log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.ERROR)

class Hotstrings(QObject):
    macro_signal = pyqtSignal()
    edit_macro_signal = pyqtSignal(object)
    quit_signal = pyqtSignal()
    program_hotstring_signal = pyqtSignal(object, str)
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.app.setStyle('fusion')
        self.linux = platform.system() == 'Linux'
        if self.linux:
            self.wayland = 'wayland' in subprocess.run(['ps', '-e', '-o', 'comm'], stdout=subprocess.PIPE).stdout.decode('utf-8').lower()
        else:
            self.wayland = False
        self.quit_requested = False
        self.macro_signal.connect(self.spawn_macro_settings)
        self.edit_macro_signal.connect(self.spawn_macro_settings)
        self.quit_signal.connect(self.exit_app)
        self.program_hotstring_signal.connect(bulk.program_hotstring_2)
        # State flags
        self.paused = False
        self.debug_flag = False
        # Used to help gather input for bulk functions
        self.bulk = None
        self.calc = Calc(self)
        self.dir = Path(__file__).parent
        self.settings_path = Path.cwd() / 'settings.json'
        if self.settings_path.exists():
            self.load_settings()
        else:
            self.endchar = '\\'
            self.user_macros = []
            self.program_hotstrings = {}
            self.save_settings()
        self.last_output = ''
        self.load_hotstrings()
        self.callables = {
            'base64': bulk.base64,
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
            'dvorak': bulk.dvorak,
            'edit macro': self.edit_macro,
            'emojify': bulk.emojify,
            'endchar': self.change_endchar,
            'flag': bulk.flag,
            'flip': bulk.flip,
            'flipcase': bulk.flip_case,
            'frac': self.calc.make_rational,
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
            'program hotstring': lambda user_input = None: bulk.program_hotstring_1(self, user_input),
            'python': bulk.python,
            'quit': self.quit_signal.emit,
            'qwerty': bulk.qwerty,
            'randomheart': bulk.random_heart,
            'record': self.start_record,
            'recordk': lambda: self.start_record(record_mouse = False),
            'recordm': lambda: self.start_record(record_keyboard = False),
            'roman': bulk.roman,
            'rot13': bulk.rot13,
            'rune': bulk.rune,
            'rune2': bulk.rune2,
            'smallcaps': bulk.smallcaps,
            'smallcaps2': bulk.smallcaps2,
            'solve': self.calc.solve,
            '__': bulk.subscript,
            '^^': bulk.superscript,
            'test': self.test_hotstrings,
            'unbase64': bulk.unbase64,
            'unbraille': bulk.unbraille,
            'underline': bulk.underline,
            'unhide': bulk.unhide,
            'U+': bulk.unicode,
            'unmorse': bulk.unmorse,
            'unroman': bulk.unroman,
            'unrune': bulk.unrune,
            'unrune2': bulk.unrune2,
            'vars': lambda: self.calc.calc('vars')
        }
        # Make sure the user_input deque is large enough to handle the largest valid hotstring
        # Make it double that length to account for things like user backspaces, arrow keys, etc
        maxlen = 0
        for key in self.Hotstrings | self.hotstrings | self.callables:
            maxlen = max(maxlen, len(key))
        self.user_input = deque(maxlen = 2*maxlen)
        self.create_tray_icon()
        if not self.wayland:
            self.mouse_listener = mouse.Listener()
        self.keyboard_listener = keyboard.Listener()
        self.create_hooks()
        self.keyboard = keyboard.Controller()
        if not self.wayland:
            self.mouse = mouse.Controller()
        self.pressed = set()
        if self.wayland:
            self.username, self.uid = self.find_wayland_user()
            if not self.username:
                raise RuntimeError('No active Wayland user found')

    def backspace(self, n):
        """Sends n backspace presses"""
        for _ in range(n):
            self.keyboard.tap(keyboard.Key.backspace)

    def change_endchar(self):
        """Changes the endchar"""
        text, ok = QInputDialog.getText(None, 'Change endchar', f'Enter the new endchar:')
        if ok and text:
            if len(text) == 1:
                self.endchar = text
                self.save_settings()
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Setting endchar failed')
                dlg.setText('Error: The endchar must be exactly 1 character. No changes made.')
                dlg.exec()

    def check_hotkeys(self):
        for hotkey in self.hotkeys:
            if self.is_hotkey_pressed(hotkey[0]):
                if self.paused and hotkey[1] != self.toggle_pause:
                    return
                hotkey[1]()
                return

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
            for program_hotstring in self.program_hotstrings:
                if typed_string.endswith(program_hotstring):
                    self.backspace(len(program_hotstring) + 1)
                    self.program_hotstring(program_hotstring)
                    return
            if match := re.search(r'(-?[\d]*\.?[\d]*)([cCfF])$', typed_string):
                # User input ended in a celsius or fahrenheit temperature like "14.7f" - convert it to the other
                self.quick_temp(match)

    def clear_hooks(self):
        if not self.wayland and self.mouse_listener.running:
            self.mouse_listener.stop()
            # The mouse listener won't actually quit until its next event - so we send a null event here
            self.mouse.move(0, 0)
            self.mouse_listener.join()
        if self.keyboard_listener.running:
            self.keyboard_listener.stop()
            # The keyboard listener won't actually quit until its next event - so we send one here
            # Don't think I can do a null event but this one seems innocuous enough
            self.keyboard.release(keyboard.Key.shift)
            self.keyboard_listener.join()
        self.hotkeys = []

    def clear_input(self, *args):
        """Clears user_input and ends any bulk collection"""
        self.user_input.clear()
        self.bulk = None

    def create_hooks(self):
        """Removes any existing hooks, then creates all the usual ones"""
        self.clear_hooks()
        if not self.wayland:
            # Clicking the mouse clears input - makes it impossible to determine what was actually typed
            self.mouse_listener = mouse.Listener(on_click = self.clear_input)
            self.mouse_listener.start()
        self.keyboard_listener = keyboard.Listener(on_press = self.handle_input_wrapper,
                                                   on_release = lambda key, injected: self.get_key_name(key, remove_from_pressed = True))
        self.keyboard_listener.start()
        self.hotkeys.append([['cmd', 'z'], self.toggle_pause])
        self.hotkeys.append([['ctrl', 'v'], self.pasted])
        for macro in self.user_macros:
            hotkey = macro[0]
            args = macro[1]
            events = args['events']
            speed_factor = args['speed_factor']
            repeat_count = args['repeat_count']
            skip_paths = args['skip_paths']
            self.hotkeys.append([hotkey, lambda: self.play(hotkey, events, speed_factor, repeat_count, skip_paths)])

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
        self.pause_menu_item = QAction('Pause')
        self.pause_menu_item.triggered.connect(self.toggle_pause)
        self.menu.addAction(self.pause_menu_item)
        # Add Change endchar option to context menu
        self.endchar_change = QAction('Change endchar')
        self.endchar_change.triggered.connect(self.change_endchar)
        self.menu.addAction(self.endchar_change)
        # Add Log Current State to context menu
        self.debug_menu_item = QAction('Enable Debug Logging')
        self.debug_menu_item.triggered.connect(self.debug)
        self.menu.addAction(self.debug_menu_item)
        # Add Exit option to context menu
        self.exit_action = QAction('Exit')
        self.exit_action.triggered.connect(self.quit_signal.emit)
        self.menu.addAction(self.exit_action)
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
        if user_input.isdigit() and 1 <= (user_int := int(user_input)) <= len(self.user_macros):
            # See if the user entered a number that corresponds to a macro - use 'macros' hotstring to see list
            macro_to_edit = self.user_macros[user_int - 1]
            self.edit_macro_signal.emit(macro_to_edit)
        else:
            return 'Invalid macro'

    def exit_app(self):
        """Quits the app"""
        self.quit_requested = True
        self.clear_hooks()
        self.tray_icon.hide()
        if self.wayland:
            self.keyboard.close()
        self.app.quit()

    def find_tray_icons(self):
        """Locates .png files to use for system tray icons, or uses default images if none are present"""
        # Define the system tray icons to be used normally, and when paused
        # Prefer local icon files if present
        normal = self.dir / 'normal.png'
        self.normal_icon = str(normal) if normal.exists() else False
        paused = self.dir / 'paused.png'
        self.paused_icon = str(paused) if paused.exists() else False
        # If no local files, try in /assets/images
        if not self.normal_icon:
            normal = self.dir.parent / 'assets/images/normal.png'
            self.normal_icon = str(normal) if normal.exists() else False
        if not self.paused_icon:
            paused = self.dir.parent / 'assets/images/paused.png'
            self.paused_icon = str(paused) if paused.exists() else False
        # If running from .exe, pyinstaller makes temp directory here, which will contain icons
        if not self.normal_icon and (meipass := getattr(sys, '_MEIPASS', False)):
            normal = Path(meipass) / 'normal.png'
            self.normal_icon = str(normal) if normal.exists() else False
        if not self.paused_icon and (meipass := getattr(sys, '_MEIPASS', False)):
            paused = Path(meipass) / 'paused.png'
            self.paused_icon = str(paused) if paused.exists() else False
        # If all else fails just use a default icon for both
        if (not self.normal_icon) or (not self.paused_icon):
            from PyQt6.QtWidgets import QStyle
        if not self.normal_icon:
            self.normal_icon = QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
        if not self.paused_icon:
            self.paused_icon = QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))

    def find_wayland_user(self):
        for uid_str in Path('/run/user').iterdir():
            path = uid_str / 'wayland-0'
            if path.exists():
                try:
                    uid_str = uid_str.name
                    username = subprocess.check_output(
                        ['getent', 'passwd', uid_str],
                        text=True
                    ).split(':')[0]
                    return username, uid_str
                except subprocess.CalledProcessError:
                    continue
        return None, None

    def get_clipboard(self, text_only = True):
        if not self.wayland:
            # This actually works fine in wayland, but pyperclip.copy() does not
            # So for consistency I use wl-clipboard for both operations in wayland for now
            return pyperclip.paste()
        # -n flag suppresses the newline otherwise appended to the end of the output
        cmd = f'XDG_RUNTIME_DIR=/run/user/{self.uid} wl-paste -n'
        result = subprocess.run(
            ['su', '-', self.username, '-c', cmd],
            capture_output=True
        )
        if result.returncode == 0:
            clipboard = result.stdout
            try:
                clipboard = clipboard.decode('utf-8')
                return clipboard
            except UnicodeDecodeError:
                # Contains something non-text, like an image or something
                if text_only:
                    return ''
                return clipboard
        else:
            return ''

    def get_key_name(self, key, add_to_pressed = False, remove_from_pressed = False):
        canonical_key = self.keyboard_listener.canonical(key)
        if hasattr(canonical_key, 'char') and canonical_key.char is not None:
            canonical_key = canonical_key.char
        elif hasattr(canonical_key, 'name') and canonical_key.name is not None:
            canonical_key = canonical_key.name
        if not isinstance(canonical_key, str) and hasattr(key, 'name'):
            canonical_key = key.name
        if add_to_pressed:
            self.pressed.add(canonical_key)
            self.check_hotkeys()
        elif remove_from_pressed:
            self.pressed.discard(canonical_key)
        if hasattr(key, 'char') and key.char is not None:
            key = key.char
        elif hasattr(key, 'name') and key.name is not None:
            key = key.name
        return key if isinstance(key, str) and key.isprintable() else None

    def get_typed_string(self, user_input, forgiving = False):
        """Parses user_input to determine what the user likely actually typed"""
        typed_string = []
        # insert_pos is only necessary to support letting the user use the left and right arrow keys
        insert_pos = 0
        if len(user_input) == 0:
            return ''
        while user_input[0] in ['left', 'right', 'backspace', 'delete', 'up', 'down']:
            # None of these events mess up the string logic when at the start of a string
            # But removing them now allows the logic below to be simpler
            del user_input[0]
            if len(user_input) == 0:
                return ''
        for i, key in enumerate(user_input):
            if key == 'delete' and self.wayland:
                key = 'backspace'
            if len(key) == 1:
                # User typed a regular character, insert it into their typed string
                typed_string.insert(insert_pos, key)
                insert_pos += 1
            elif key == 'space':
                typed_string.insert(insert_pos, ' ')
                insert_pos += 1
            elif key == 'left':
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
            elif key == 'right':
                insert_pos += 1
                if insert_pos > len(typed_string):
                    # If they tried to move right of the rightmost position, we have no
                    # way of knowing what their input looks like - so just give up
                    # Or if we're feeling forgiven, start over from here
                    if not forgiving:
                        return None
                    typed_string = []
                    insert_pos = 0
            elif key in ['up', 'down']:
                # Both of these keys make it impossible to accurately
                # determine what the user input looks like, give up
                # Or if we're feeling forgiven, start over from here
                if not forgiving:
                    return None
                typed_string = []
                insert_pos = 0
            elif key == 'backspace':
                if insert_pos >= 1:
                    del typed_string[insert_pos - 1]
                    insert_pos -= 1
            elif key == 'enter':
                typed_string.insert(insert_pos, '\n')
                insert_pos += 1
            elif key == 'tab':
                typed_string.insert(insert_pos, '\t')
                insert_pos += 1
            elif key.startswith('_paste_'):
                for char in key[7:]:
                    typed_string.insert(insert_pos, char)
                    insert_pos += 1
        return ''.join(typed_string[:insert_pos])

    def handle_input(self, key):
        """Handles all input"""
        if self.paused:
            # Do nothing if we're paused
            return
        if key == self.endchar:
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
                    text = self.get_clipboard()
                    if not isinstance(text, str):
                        self.bulk = None
                        return
                    if len(text) > self.bulk['max'] or not isinstance(text, str):
                        # Give up and do nothing if there's too much text in the clipboard (or if it isn't a string)
                        self.bulk = None
                        return
                try:
                    # Send the input to the function
                    if isinstance(text, str):
                        output = self.bulk['func'](text)
                    else:
                        output = None
                    if self.bulk['func'] == self.calc.calculator and output == 'end_calculator':
                        # Calculator sends that output when it's time to quit
                        # Remove 'func' so below code will properly exit
                        self.bulk['func'] = None
                        output = ''
                    # Backspace all the user input
                    self.backspace(backspace_count)
                    # Write the function output
                    if isinstance(output, str):
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
                self.user_input.append(key)
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
            self.bulk['input'].append(key)
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
            if key != 'v' or 'ctrl' not in self.pressed:
                self.user_input.append(key)

    def handle_input_wrapper(self, key, injected = False):
        """Calls handle_input, logs current state in event of errors"""
        if injected:
            return
        try:
            if self.debug_flag: self.log_state()
            key = self.get_key_name(key, add_to_pressed = True)
            if key is None:
                return
            self.handle_input(key)
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

    def is_any_pressed(self, keys):
        return any(key in self.pressed for key in keys)

    def is_hotkey_pressed(self, keys):
        for key in self.pressed:
            if key in {'ctrl', 'alt', 'shift', 'cmd'} and key not in keys:
                return False
        return all(key in self.pressed for key in keys)

    def load_hotstrings(self):
        """Reads the hotstrings.json file and loads it into memory"""
        # Prefer a hotstrings.json in the cwd if it exists
        hotstrings_path = self.dir / 'hotstrings.json'
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
            self.user_macros = self.serialize_user_macros(deserialize = self.user_macros)
        else:
            self.user_macros = []
        if 'user_vars' in settings:
            user_vars = settings['user_vars']
            for key, value in user_vars.items():
                if isinstance(value, str):
                    user_vars[key] = complex(value)
            self.calc.user_vars = user_vars
        if 'user_funcs_raw' in settings:
            self.calc.user_funcs_raw = settings['user_funcs_raw']
        if 'program_hotstrings' in settings:
            self.program_hotstrings = settings['program_hotstrings']
        else:
            self.program_hotstrings = {}
        self.calc.update_user_funcs()

    def log_state(self):
        """Adds current values various variables to the log file"""
        log_message = ['LOGGING CURRENT STATE']
        log_message.append(f'{self.endchar = }')
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
            output.append(f'{i}: {macro[0]}')
        if output:
            return 'User macros:\n' + '\n'.join(output)
        else:
            return 'No user macros defined.'

    def on_click(self, x, y, button, pressed, injected):
        event_type = 'mouse_click' if pressed else 'mouse_release'
        return {'event_type': event_type,
                'time': time.time(),
                'device': 'mouse',
                'pos': (x, y),
                'button': button}

    def on_move(self, x, y, injected):
        return {'event_type': 'mouse_move',
                'time': time.time(),
                'device': 'mouse',
                'pos': (x, y)}

    def on_press(self, key, injected):
        return {'event_type': 'key_down',
                'time': time.time(),
                'device': 'keyboard',
                'key': key,
                'name': self.get_key_name(key, add_to_pressed = True)}

    def on_release(self, key, injected):
        return {'event_type': 'key_up',
                'time': time.time(),
                'device': 'keyboard',
                'key': key,
                'name': self.get_key_name(key, remove_from_pressed = True)}

    def on_scroll(self, x, y, dx, dy, injected):
        return {'event_type': 'mouse_scroll',
                'time': time.time(),
                'device': 'mouse',
                'pos': (x, y),
                'scroll': (dx, dy)}

    def on_tray_icon_activated(self, reason):
        """Pauses the app when system tray icon is double clicked"""
        # This function basically just makes sure it takes a double click, not a single click, to do this
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.toggle_pause()

    def pasted(self):
        """Detects paste events, adds them to bulk input"""
        # Custom way I store paste events
        paste_event = '_paste_' + self.get_clipboard()
        if self.bulk:
            self.bulk['input'].append(paste_event)
        else:
            self.user_input.append(paste_event)

    def play(self, hotkey, events, speed_factor, repeat_count, skip_paths):
        """Plays back a macro"""
        # Remove all hooks for playback
        self.clear_hooks()
        self.pressed = set()
        self.keyboard_listener = keyboard.Listener(on_press = self.on_press,
                                                   on_release = self.on_release)
        self.keyboard_listener.start()
        while repeat_count > 0:
            for i, event in enumerate(events):
                if self.is_hotkey_pressed(hotkey):
                    # If the user is pressing the hotkey, wait for them to let go, then end the macro and rebuild hooks
                    while self.is_hotkey_pressed(hotkey):
                        time.sleep(0.01)
                    return self.create_hooks()
                # Timing loop:
                if i > 0:
                    # First event always starts immediately
                    # Wait the amount of time between this event and the previous one, divided by the speed factor
                    go_time = time.time() + (event['time'] - events[i-1]['time']) / speed_factor
                    while (current_time := time.time()) < go_time:
                        if self.is_hotkey_pressed(hotkey):
                            # If the macro hotkey is pressed, end the macro and rebuildhooks
                            while self.is_hotkey_pressed(hotkey):
                                time.sleep(0.01)
                            return self.create_hooks()
                        # Sleep in .01 second increments or less, until enough time has elapsed
                        time.sleep(min(0.01, go_time - current_time))
                # Processes each kind of event that can be encountered, and carries it out
                if event['event_type'] == 'mouse_click': # Mouse was clicked
                    self.mouse.position = event['pos']
                    self.mouse.press(event['button'])
                elif event['event_type'] == 'mouse_release':
                    self.mouse.position = event['pos']
                    self.mouse.release(event['button'])
                elif event['event_type'] == 'mouse_move' and not skip_paths: # Mouse was moved
                    self.mouse.position = event['pos']
                elif event['event_type'] == 'mouse_scroll': # Mouse wheel was scrolled
                    self.mouse.position = event['pos']
                    self.mouse.scroll(*event['scroll'])
                elif event['event_type'] == 'key_down': # Keyboard key was pressed
                    self.keyboard.press(event['key'])
                elif event['event_type'] == 'key_up':
                    self.keyboard.release(event['key'])
            repeat_count -= 1
        # All done, rebuild hooks
        return self.create_hooks()

    def program_hotstring(self, name):
        """Opens the specified file in a new process - useful for launching programs with hotstrings"""
        file_path = Path(self.program_hotstrings[name])
        file_cwd = str(file_path.parent)
        file_path = str(file_path)
        subprocess.Popen([file_path],
                         cwd = file_cwd,
                         start_new_session = True,
                         shell = True)

    def quick_temp(self, match):
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

    def record(self, event):
        """Records keyboard and mouse events to create a macro"""
        if event['event_type'] == 'key_down' and event['name'] == self.endchar:
            # Endchar is encountered, end collection
            self.create_hooks()
            # It will usually catch the keyboard up event for the endchar that activated recording
            # So find and remove it
            for i, event in enumerate(self.events):
                if event['device'] == 'keyboard':
                    if event['event_type'] == 'key_up' and event['name'] == self.endchar:
                        del self.events[i]
                    # If present it'll always be the first KeyboardEvent, so break if we find one and it isn't
                    break
            # Index all times from the start of the first event, which is our t = 0
            start_time = self.events[0]['time']
            for i, event in enumerate(self.events):
                self.events[i]['time'] = event['time'] - start_time
            # Remove the endchar
            self.backspace(1)
            # Spawn the macro settings window
            self.macro_signal.emit()
        else:
            if self.record_keyboard and event['device'] == 'keyboard':
                self.events.append(event)
            elif self.record_mouse and event['device'] == 'mouse':
                self.events.append(event)

    def save_settings(self):
        """Saves current settings to file"""
        settings = {}
        settings['endchar'] = self.endchar
        settings['user_macros'] = self.serialize_user_macros()
        settings['program_hotstrings'] = self.program_hotstrings
        settings['user_vars'] = self.calc.user_vars
        settings['user_funcs_raw'] = self.calc.user_funcs_raw
        for key, value in settings['user_vars'].items():
            if isinstance(value, complex):
                settings['user_vars'][key] = str(value)
        with open(self.settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)

    def serialize_user_macros(self, deserialize = None):
        if deserialize:
            new_macros = deserialize
            for i, macro in enumerate(new_macros):
                for j, event in enumerate(macro[1]['events']):
                    if 'key' in event:
                        key_type, value = event['key'].split(':')
                        if key_type == 'key':
                            new_macros[i][1]['events'][j]['key'] = getattr(keyboard.Key, value, None)
                        elif key_type == 'keycode':
                            new_macros[i][1]['events'][j]['key'] = keyboard.KeyCode.from_char(value)
                    elif 'button' in event:
                        new_macros[i][1]['events'][j]['button'] = getattr(mouse.Button, event['button'], None)
        else:
            new_macros = self.user_macros
            for i, macro in enumerate(new_macros):
                for j, event in enumerate(macro[1]['events']):
                    if 'key' in event:
                        key = event['key']
                        if isinstance(key, keyboard.Key):
                            new_macros[i][1]['events'][j]['key'] = f'key:{key.name}'
                        elif isinstance(key, keyboard.KeyCode):
                            new_macros[i][1]['events'][j]['key'] = f'keycode:{key.char}'
                    elif 'button' in event:
                        new_macros[i][1]['events'][j]['button'] = event['button'].name
        return new_macros

    def set_clipboard(self, text):
        #return pyperclip.copy(text)
        if not self.wayland:
            # pyperclip works in wayland, but the copy function is very slow for some reason
            return pyperclip.copy(text)
        if isinstance(text, str):
            cmd = f'XDG_RUNTIME_DIR=/run/user/{self.uid} WAYLAND_DISPLAY=wayland-0 wl-copy'
            subprocess.run(
                ['su', '-', self.username, '-c', cmd],
                input=text,
                text=True
            )
        elif isinstance(text, bytes):
            cmd = f'XDG_RUNTIME_DIR=/run/user/{self.uid} wl-copy'
            subprocess.run(
                ['su', '-', self.username, '-c', cmd],
                input=text
            )

    def spawn_macro_settings(self, macro = None):
        """Opens the window to configure and save macros"""
        try:
            if macro:
                # User is editing an existing macro
                self.settings = Macro_Settings(self, None, macro)
                self.user_macros.remove(macro)
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
        self.record_keyboard = record_keyboard
        self.record_mouse = record_mouse and not self.wayland
        # Remove all hooks so we can redirect them to the recorder
        self.clear_hooks()
        # Keyboard data is always sent to the recorder, even if we aren't saving it, for endchar detection
        self.keyboard_listener = keyboard.Listener(on_press = lambda key, injected: self.record(self.on_press(key, injected)),
                                                   on_release = lambda key, injected: self.record(self.on_release(key, injected)))
        self.keyboard_listener.start()
        # Only bother sending mouse data to the recorder if we're actually recording it
        if self.record_mouse:
            self.mouse_listener = mouse.Listener(on_move = lambda x, y, injected: self.record(self.on_move(x, y, injected)),
                                                 on_click = lambda x, y, button, pressed, injected: self.record(self.on_click(x, y, button, pressed, injected)),
                                                 on_scroll = lambda x, y, dx, dy, injected: self.record(self.on_scroll(x, y, dx, dy, injected)))
            self.mouse_listener.start()

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
        if not text or not isinstance(text, str): return
        text = text.encode('utf-8').decode('utf-8')
        while '\n' in text:
            # It works without doing this, but it works as if just pressing 'enter'
            # In chat programs like discord this automatically sends messages, which is annoying
            # So this enters linebreaks as shift+enter instead, to avoid that
            index = text.index('\n')
            if self.wayland:
                self.write_wayland(text[:index])
            elif self.linux:
                self.write_linux(text[:index])
            else:
                self.write_linux(text[:index])
                #self.keyboard.type(text[:index])
            with self.keyboard.pressed(keyboard.Key.shift):
                self.keyboard.tap(keyboard.Key.enter)
            text = text[index + 1:]
        if self.wayland:
            self.write_wayland(text)
        elif self.linux:
            self.write_linux(text)
        else:
            self.write_linux(text)
            #self.keyboard.type(text)
        # Save the last output, which is used to define the special '_' variable
        self.last_output = text

    def write_linux(self, text):
        """Writes the provided text, avoids using pynput's self.keyboard.type to do so due to an X11-specific bug with it"""
        clipboard = self.get_clipboard(text_only = False)
        self.set_clipboard(text)
        with self.keyboard.pressed(keyboard.Key.ctrl):
            self.keyboard.tap(keyboard.KeyCode.from_char('v'))
        # Without the sleep before restoring the clipboard, the pasted content is sometimes just the restored clipboard content
        time.sleep(.15)
        self.set_clipboard(clipboard)

    def write_wayland(self, text):
        """Writes the provided text, works in Wayland"""
        clipboard = self.get_clipboard(text_only = False)
        self.set_clipboard(text)
        # This code would be nice, but does not work for whatever reason
        # Gets interpreted more like Alt+v than Ctrl+v
        with self.keyboard.pressed(keyboard.Key.ctrl):
            self.keyboard.tap(keyboard.KeyCode.from_char('v'))
        self.set_clipboard(clipboard)

def main():
    hotstrings = Hotstrings(QApplication([]))
    def excepthook(exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
        else:
            traceback.print_exception(exc_type, exc_value, exc_tb)
    #sys.excepthook = excepthook
    while not hotstrings.quit_requested:
        hotstrings.app.exec()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        logging.exception('Unhandled exception in main\n')
