import evdev
import threading
from evdev import InputDevice, categorize, ecodes, UInput
from pynput.keyboard import Key, KeyCode
from contextlib import contextmanager

# Key maps for printable characters
key_map = {
    'KEY_A': 'a', 'KEY_B': 'b', 'KEY_C': 'c', 'KEY_D': 'd',
    'KEY_E': 'e', 'KEY_F': 'f', 'KEY_G': 'g', 'KEY_H': 'h',
    'KEY_I': 'i', 'KEY_J': 'j', 'KEY_K': 'k', 'KEY_L': 'l',
    'KEY_M': 'm', 'KEY_N': 'n', 'KEY_O': 'o', 'KEY_P': 'p',
    'KEY_Q': 'q', 'KEY_R': 'r', 'KEY_S': 's', 'KEY_T': 't',
    'KEY_U': 'u', 'KEY_V': 'v', 'KEY_W': 'w', 'KEY_X': 'x',
    'KEY_Y': 'y', 'KEY_Z': 'z',
    'KEY_1': '1', 'KEY_2': '2', 'KEY_3': '3', 'KEY_4': '4',
    'KEY_5': '5', 'KEY_6': '6', 'KEY_7': '7', 'KEY_8': '8',
    'KEY_9': '9', 'KEY_0': '0',
    'KEY_SPACE': ' ', 'KEY_ENTER': '\n', 'KEY_DOT': '.', 'KEY_COMMA': ',',
    'KEY_MINUS': '-', 'KEY_EQUAL': '=', 'KEY_SLASH': '/', 'KEY_BACKSLASH': '\\',
    'KEY_SEMICOLON': ';', 'KEY_APOSTROPHE': "'", 'KEY_LEFTBRACE': '[', 'KEY_RIGHTBRACE': ']',
    'KEY_GRAVE': '`'
}

# Shift-modified equivalents for special characters
shift_map = {
    '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
    '-': '_', '=': '+', '[': '{', ']': '}', '\\': '|',
    ';': ':', "'": '"', ',': '<', '.': '>', '/': '?', '`': '~'
}

def find_keyboard():
    devices = [evdev.InputDevice(p) for p in evdev.list_devices()]
    for d in devices:
        if 'keyboard' in d.name.lower():
            return d
    raise RuntimeError("No keyboard device found.")

# In evput/keyboard.py or in the same file

class Key:
    # Define special keys like in pynput
    shift = 'shift'
    ctrl = 'ctrl_l'
    ctrl_l = 'ctrl_l'
    ctrl_r = 'ctrl_r'
    alt_l = 'alt_l'
    alt_r = 'alt_r'
    caps_lock = 'caps_lock'
    enter = 'enter'
    space = 'space'
    backspace = 'backspace'
    tab = 'tab'
    esc = 'esc'
    left = 'left'
    right = 'right'
    up = 'up'
    down = 'down'
    insert = 'insert'
    delete = 'delete'
    home = 'home'
    end = 'end'
    page_up = 'page_up'
    page_down = 'page_down'
    num_lock = 'num_lock'
    f1 = 'f1'
    f2 = 'f2'
    f3 = 'f3'
    f4 = 'f4'
    f5 = 'f5'
    f6 = 'f6'
    f7 = 'f7'
    f8 = 'f8'
    f9 = 'f9'
    f10 = 'f10'
    f11 = 'f11'
    f12 = 'f12'

    # Map to handle key codes
    @staticmethod
    def from_char(char):
        return KeyCode.from_char(char)

class Controller:
    def __init__(self):
        self._device = UInput({
            ecodes.EV_KEY: [ecodes.KEY_LEFTCTRL, ecodes.KEY_V, ecodes.KEY_BACKSPACE],
            ecodes.EV_SYN: []
        })
        self._pressed_keys = set()

    def close(self):
        self._device.close()

    def _press_key(self, key):
        #if isinstance(key, KeyCode):
        #    key = key.char
        #elif isinstance(key, Key):
        #    key = key.name.lower()
        if key not in self._pressed_keys:
            self._send_event(key, ecodes.EV_KEY, 1)
            self._pressed_keys.add(key)

    def _release_key(self, key):
        #if isinstance(key, KeyCode):
        #    key = key.char
        #elif isinstance(key, Key):
        #    key = key.name.lower()

        if key in self._pressed_keys:
            self._send_event(key, ecodes.EV_KEY, 0)
            self._pressed_keys.remove(key)

    def _send_event(self, key, ev_type, ev_value):
        import evdev.ecodes as ec
        # Handle KeyCode (character keys)
        if isinstance(key, KeyCode):
            char = key.char.lower()
            for code, mapped_char in key_map.items():
                if mapped_char == char:
                    key_code = getattr(ec, code)
                    break
            else:
                return  # Unknown key, skip
        elif isinstance(key, Key):
            name = key.name.lower()
            key_code = getattr(ec, f'KEY_{name.upper()}', None)
            if key_code is None:
                return  # Unknown special key
        elif isinstance(key, str):
            special_keys = {
                'ctrl_l': ecodes.KEY_LEFTCTRL,
                'ctrl_r': ecodes.KEY_RIGHTCTRL,
                'shift': ecodes.KEY_LEFTSHIFT,
                'shift_r': ecodes.KEY_RIGHTSHIFT,
                'alt_l': ecodes.KEY_LEFTALT,
                'alt_r': ecodes.KEY_RIGHTALT,
                'backspace': ecodes.KEY_BACKSPACE,
                'enter': ecodes.KEY_ENTER,
                'space': ecodes.KEY_SPACE,
                'tab': ecodes.KEY_TAB,
                'esc': ecodes.KEY_ESC,
                # Add more as needed
            }
            if len(key) == 1:
                return self._send_event(KeyCode.from_char(key), ev_type, ev_value)
            else:
                key_code = special_keys.get(key.lower(), getattr(ec, f'KEY_{key.upper()}', None))
                if key_code is None:
                    return
        else:
            return
        self._device.write(ec.EV_KEY, key_code, ev_value)
        self._device.write(ec.EV_SYN, 0, 0)
        self._device.syn()


    def press(self, key):
        """Press a single key."""
        self._press_key(key)

    def release(self, key):
        """Release a single key."""
        self._release_key(key)

    def tap(self, key):
        """Tap a single key: press and release."""
        self.press(key)
        self.release(key)

    def type(self, text):
        """Type a string by tapping each character."""
        for char in text:
            key = KeyCode.from_char(char)
            self.tap(key)

    @contextmanager
    def pressed(self, key):
        self.press(key)
        try:
            yield
        finally:
            self.release(key)

class Listener:
    def __init__(self, on_press=None, on_release=None):
        self.on_press = on_press
        self.on_release = on_release
        self._running = False
        self._thread = None
        self._stop_flag = threading.Event()
        self._device = find_keyboard()
        self._shift = False
        self._caps = False

    @property
    def running(self):
        return self._running

    def canonical(self, key):
        # If it's already a Key or KeyCode, return as-is
        from pynput.keyboard import Key, KeyCode

        if isinstance(key, (Key, KeyCode)):
            return key

        # If it's a single character string, return KeyCode
        if isinstance(key, str) and len(key) == 1:
            return KeyCode.from_char(key)

        # If it's a named key string like 'ctrl_l', return Key
        if isinstance(key, str):
            return getattr(Key, key, key)

        return key

    def start(self):
        if self._running:
            return
        self._stop_flag.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_flag.set()

    def join(self):
        if self._thread:
            self._thread.join()

    def _translate(self, keycode):
        char = key_map.get(keycode)
        if not char:
            return None
        if char.isalpha():
            return char.upper() if self._caps ^ self._shift else char.lower()
        elif self._shift:
            return shift_map.get(char, char)
        else:
            return char

    def _run(self):
        self._running = True
        try:
            for event in self._device.read_loop():
                if self._stop_flag.is_set():
                    break
                if event.type != ecodes.EV_KEY:
                    continue

                key_event = categorize(event)
                keycode = key_event.keycode
                is_down = key_event.keystate == key_event.key_down
                is_up = key_event.keystate == key_event.key_up

                # Handle modifier keys (Shift, CapsLock)
                if keycode in ('KEY_LEFTSHIFT', 'KEY_RIGHTSHIFT'):
                    self._shift = is_down
                    continue
                elif keycode == 'KEY_CAPSLOCK' and is_down:
                    self._caps = not self._caps
                    continue

                # Translate to correct character
                char = self._translate(keycode)
                if is_down and self.on_press:
                    # Create KeyCode or Key object
                    if char:
                        key = KeyCode.from_char(char)
                    else:
                        key = getattr(Key, keycode.replace('KEY_', '').lower(), None)
                    self.on_press(key, False)
                elif is_up and self.on_release:
                    # Same for release
                    if char:
                        key = KeyCode.from_char(char)
                    else:
                        key = getattr(Key, keycode.replace('KEY_', '').lower(), None)
                    self.on_release(key, False)
        finally:
            self._running = False
