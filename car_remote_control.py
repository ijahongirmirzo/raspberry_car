from pynput import keyboard
from car_control import *

keys = keyboard.Key
PRESSED_KEYS_COUNT = 0


def on_press(key):
    if not hasattr(globals, 'PRESSED_KEYS_COUNT'):
        print('initialized on press')
        global PRESSED_KEYS_COUNT
    print("%s is pressed" % key)
    if key == keys.up:
        return forward()
    if key == keys.down:
        return backward()
    if key == keys.right:
        return right()
    if key == keys.left:
        return left()


def on_release(key):
    print("%s is released" % key)
    if key in [keys.up, keys.down, keys.right, keys.left]:
        destroy()


if __name__ == '__main__':
    pressed_keys_count = 0
    setup()
    # while True:
    #     print(get_distance())
    #     time.sleep(0.5)
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
