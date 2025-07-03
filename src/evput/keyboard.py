import evdev
import pynput.keyboard._uinput as keyboard
from pynput.keyboard._uinput import Key
import time

class Layout(keyboard.Layout):
    def __init__(self):
        super().__init__()
        # Fixes two bugs with self._char_table present in Pynput that set modifiers incorrectly
        def as_char(k):
            return k.value.char if isinstance(k, Key) else k.char
        self._char_table = {
            as_char(key): (
                vk,
                set()
                    | ({Key.shift} if i & 1 else set())
                    | ({Key.alt_gr} if i & 2 else set()))
            for vk, keys in self._vk_table.items()
            for i, key in reversed(list(enumerate(keys)))
            if key is not None and as_char(key) is not None}

class Controller(keyboard.Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._layout = Layout()

    # Same as the original _handle, but fixes two Pynput bugs
    def _handle(self, key, is_press):
        # Resolve the key to a virtual key code and a possible set of required
        # modifiers
        try:
            vk, required_modifiers = self._to_vk_and_modifiers(key)
        except ValueError:
            raise self.InvalidKeyException(key)

        # Determine how we need to modify the modifier state
        if is_press and required_modifiers: # This line modified
            with self.modifiers as modifiers:
                vk, required_modifiers = self._layout.for_char(key.char)
                to_press = {
                    getattr(evdev.ecodes, key.value._kernel_name)
                    for key in (required_modifiers - modifiers)}
                to_release = {
                    getattr(evdev.ecodes, key.value._kernel_name)
                    for key in (modifiers - required_modifiers)
                    } & {Key.shift, Key.alt_gr} # This line modified
        else:
            to_release = set()
            to_press = set()

        # Update the modifier state, send the key, and finally release any
        # modifiers
        cleanup = []
        try:
            for k in to_release:
                self._send(k, False)
                cleanup.append((k, True))
            for k in to_press:
                self._send(k, True)
                cleanup.append((k, False))

            self._send(vk, is_press)

        finally:
            for e in reversed(cleanup):
                # pylint: disable E722; we want to suppress exceptions
                try:
                    self._send(*e)
                except:
                    pass
                # pylint: enable E722

            self._dev.syn()

    # Adds support for typing arbitrary unicode characters
    # Does so with Linux Ctrl+Shift+U, then unicode codepoint, then space feature
    # Only works in GTK apps
    def press(self, key):
        try:
            return super().press(key)
        except KeyError:
            uni = hex(ord(key))[2:].lower()
            self._dev.write(1, 29, 1) # Ctrl down
            self._dev.write(1, 42, 1) # Shift down
            self._dev.write(1, 22, 1) # u down
            self._dev.write(1, 22, 0) # u up
            self._dev.write(1, 42, 0) # Shift up
            self._dev.write(1, 29, 0) # Ctrl up
            for char in uni:
                vk, _ = self._layout.for_char(char)
                self._dev.write(1, vk, 1) # char down
                self._dev.write(1, vk, 0) # char up
            self._dev.write(1, 57, 1) # Space down
            self._dev.write(1, 57, 0) # Space up
            self._dev.syn()
            time.sleep(0.005) # For large strings of unsupported characters, it often fails without this
            return

    def release(self, key):
        try:
            return super().release(key)
        except KeyError:
            return

class Listener(keyboard.Listener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # This is similarly only to work around a bug in Pynput
    # Can remove this entire file if bugs are fixed
    # https://github.com/moses-palmer/pynput/issues/658
    def _device(self, paths, first_try = True):
        """Attempts to load a readable keyboard device.

        :param paths: A list of paths.

        :return: a compatible device
        """
        dev, count = None, 0
        for path in paths:
            # Open the device
            try:
                next_dev = evdev.InputDevice(path)
            except OSError:
                continue
            if first_try and 'keyboard' not in next_dev.name.lower():
                next_dev.close()
                continue
            # Does this device provide more handled event codes?
            capabilities = next_dev.capabilities()
            next_count = sum(
                len(codes)
                for event, codes in capabilities.items()
                if event in self._EVENTS)
            if next_count > count:
                dev = next_dev
                count = next_count
            else:
                next_dev.close()

        if dev is None:
            if first_try:
                return self._device(paths, first_try = False)
            raise OSError('no keyboard device available')
        else:
            return dev
