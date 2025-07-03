import time

import evdev
from evdev import UInput, categorize, ecodes as e

import pynput.mouse._base as mouse
from pynput.mouse._base import Button
from pynput._util.uinput import ListenerMixin

class Controller(mouse.Controller):
    def __init__(self):
        super().__init__()
        capabilities = {
            e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT, e.BTN_MIDDLE, e.BTN_SIDE, e.BTN_EXTRA, e.BTN_FORWARD, e.BTN_BACK, e.BTN_TASK],
            e.EV_REL: [e.REL_X, e.REL_Y, e.REL_HWHEEL, e.REL_WHEEL, e.REL_WHEEL_HI_RES, e.REL_HWHEEL_HI_RES]
        }
        self._dev = UInput(capabilities, name="evput mouse")

    def __del__(self):
        if hasattr(self, '_dev'):
            self._dev.close()

    def scroll(self, dx = 0, dy = 0):
        return self._scroll(dx, dy)

    def _scroll(self, dx = 0, dy = 0):
        if dx:
            self._dev.write(e.EV_REL, e.REL_HWHEEL, dx)
        if dy:
            self._dev.write(e.EV_REL, e.REL_WHEEL, dy)
        if dx or dy:
            self._dev.syn()

    def _press(self, button):
        """The implementation of the :meth:`press` method.

        This is a platform dependent implementation.
        """
        if button == Button.left:
            self._dev.write(e.EV_KEY, e.BTN_LEFT, 1)
        elif button == Button.middle:
            self._dev.write(e.EV_KEY, e.BTN_MIDDLE, 1)
        elif button == Button.right:
            self._dev.write(e.EV_KEY, e.BTN_RIGHT, 1)
        if button in [Button.left, Button.middle, Button.right]:
            self._dev.syn()

    def _release(self, button):
        """The implementation of the :meth:`release` method.

        This is a platform dependent implementation.
        """
        if button == Button.left:
            self._dev.write(e.EV_KEY, e.BTN_LEFT, 0)
        elif button == Button.middle:
            self._dev.write(e.EV_KEY, e.BTN_MIDDLE, 0)
        elif button == Button.right:
            self._dev.write(e.EV_KEY, e.BTN_RIGHT, 0)
        if button in [Button.left, Button.middle, Button.right]:
            self._dev.syn()

    def move(self, dx, dy):
        if dx:
            self._dev.write(e.EV_REL, e.REL_X, dx)
        if dy:
            self._dev.write(e.EV_REL, e.REL_Y, dy)
        if dx or dy:
            self._dev.syn()

class Listener(ListenerMixin, mouse.Listener):
    _EVENTS = (e.EV_KEY, e.EV_REL)
    def __init__(self, *args, **kwargs):
        super(Listener, self).__init__(*args, **kwargs)
        self._dev = self._get_device()

    def _handle_message(self, event):
        if event.type == e.EV_KEY:  # Button events
            key_event = categorize(event)
            if key_event.event.value == 1:  # Button press
                self.on_click(key_event.keycode, False)
            elif key_event.event.value == 0:  # Button release
                pass
        elif event.type == e.EV_REL:  # Motion events
            if event.code == e.REL_X:
                self.on_move(event.value, 0, False)
            elif event.code == e.REL_Y:
                self.on_move(0, event.value, False)
            elif event.code == e.REL_WHEEL:
                self.on_scroll(0, event.value, False)
            elif event.code == e.REL_HWHEEL:
                self.on_scroll(event.value, 0, False)

    def _get_device(self):
        """Attempts to load a readable mouse device.

        :param paths: A list of paths.

        :return: a compatible device
        """
        dev, count = None, 0
        paths = evdev.list_devices()
        required_events = {
            e.REL_X, e.REL_Y,  # Movement events
            e.BTN_LEFT, e.BTN_RIGHT  # Button events
        }
        for path in paths:
            # Open the device
            try:
                next_dev = evdev.InputDevice(path)
            except OSError:
                continue
            # Does this device provide more handled event codes?
            capabilities = next_dev.capabilities()
            # Check if the device supports the required events
            if not all(event in capabilities.get(e.EV_REL, []) for event in [e.REL_X, e.REL_Y]):
                next_dev.close()
                continue

            if not all(event in capabilities.get(e.EV_KEY, []) for event in [e.BTN_LEFT, e.BTN_RIGHT]):
                next_dev.close()
                continue
            next_count = sum(
                len(codes)
                for event, codes in capabilities.items()
                if event in {e.EV_REL, e.EV_ABS})
            if next_count > count:
                dev = next_dev
                count = next_count
            else:
                next_dev.close()

        if dev is None:
            raise OSError('no mouse device available')
        else:
            return dev
