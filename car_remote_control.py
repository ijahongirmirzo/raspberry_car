from pynput import keyboard
from car_details import *
import time

keys = keyboard.Key
PRESSED_KEYS_COUNT = 0

def on_press(key):
    if not hasattr(globals, 'PRESSED_KEYS_COUNT'):
        print('initialized on press')
        global PRESSED_KEYS_COUNT
        PRESSED_KEYS_COUNT = 0
    print ("%s is pressed" % key)
    if key in [keys.up, keys.down, keys.right, keys.left]:
        PRESSED_KEYS_COUNT = PRESSED_KEYS_COUNT + 1
        print("release count %s" % PRESSED_KEYS_COUNT)
        if key == keys.up:
            # if get_distance() >= 20:
            trace = get_trace()
            print(trace)
            if trace == STRAIGHT:
                return forward()
            elif trace == RIGHT:
                return right()
            elif trace == LEFT:
                return left()
            elif trace == STOP:
                return stop()

        if key == keys.down:
            return backward()
        if key == keys.right:
            return right()
        if key == keys.left:
            return left()

    

def on_release(key):
    if not hasattr(globals, 'PRESSED_KEYS_COUNT'):
        print('initialized on release')
        global PRESSED_KEYS_COUNT
        PRESSED_KEYS_COUNT = 0
    print ("%s is released" % key)
    if key in [keys.up, keys.down, keys.right, keys.left]:
        print("release count %s" % PRESSED_KEYS_COUNT)
        PRESSED_KEYS_COUNT = PRESSED_KEYS_COUNT - 1
        if PRESSED_KEYS_COUNT <= 0:
            stop()


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
