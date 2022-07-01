from typing import cast
import pynput
import sys
import pyperclip
import uuid

if sys.platform == "darwin":
    TRIGGER_BASE = f"<cmd>+<shift>"
    SHORTCUT_KEY = cast(str, pynput.keyboard.Key.cmd.value)
else:
    TRIGGER_BASE = f"<ctrl>+<shift>"
    SHORTCUT_KEY = cast(str, pynput.keyboard.Key.ctrl.value)
SHIFT_KEY = cast(str, pynput.keyboard.Key.shift.value)


def copy_paste_uuid(keyboard_controller: pynput.keyboard.Controller):
    pyperclip.copy(str(uuid.uuid4()))
    keyboard_controller.release(SHIFT_KEY)
    keyboard_controller.press(SHORTCUT_KEY)
    keyboard_controller.press("v")
    keyboard_controller.release("v")
    keyboard_controller.release(SHORTCUT_KEY)


def main():
    keyborad_controller = pynput.keyboard.Controller()
    try:
        with pynput.keyboard.GlobalHotKeys(
            {
                f"{TRIGGER_BASE}+v": lambda: copy_paste_uuid(keyborad_controller),
            }
        ) as h:
            h.join()
    except:
        print("\nBye")


if __name__ == "__main__":
    main()
