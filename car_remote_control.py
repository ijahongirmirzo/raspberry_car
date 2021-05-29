from pynput import keyboard
from car_details import *

from constants import STOP, FORWARD, RIGHT, LEFT

keys = keyboard.Key
PRESSED_KEYS_COUNT = 0


def on_press(key):
    print("%s is pressed" % key)
    if key == keys.up:
        # return forward(slowness_time=3)
        trace = get_trace()
        if trace == RIGHT:
            return smooth_right()
        elif trace == LEFT:
            return smooth_left()
        elif trace == STOP:
            return stop()
        elif trace == FORWARD:
            return forward(3)

    if key == keys.down:
        return backward()
    if key == keys.right:
        return right()
    if key == keys.left:
        return left()


def on_release(key):
    print("%s is released" % key)
    if key in [keys.up, keys.down, keys.right, keys.left]:
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
