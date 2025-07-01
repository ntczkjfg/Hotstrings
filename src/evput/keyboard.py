import evdev
import pynput.keyboard._uinput as keyboard
from pynput.keyboard._uinput import Key

class Controller(keyboard.Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # This is only to work around a few bugs in Pynput
    # Will remove if bugs are fixed
    # https://github.com/moses-palmer/pynput/issues/657
    def _to_vk_and_modifiers(self, key):
        vk, required_modifiers = super()._to_vk_and_modifiers(key)
        if required_modifiers:
            required_modifiers.discard(Key.alt_gr)
        if not required_modifiers:
            required_modifiers = None
        return (vk, required_modifiers)

class Listener(keyboard.Listener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'keyboard' not in self._dev.name.lower():
            self._dev = self.find_keyboard()
    # This is similarly only to work around a bug in Pynput
    # Can remove this entire file if bugs are fixed
    # https://github.com/moses-palmer/pynput/issues/658
    def find_keyboard(self):
        devices = [evdev.InputDevice(p) for p in evdev.list_devices()]
        for d in devices:
            if 'keyboard' in d.name.lower():
                return d
        raise OSError('no keyboard device available')
