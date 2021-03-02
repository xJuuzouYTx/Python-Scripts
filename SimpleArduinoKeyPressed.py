from pynput.keyboard import Key, Listener
import serial
s = serial.Serial('COM12', 9600)

def on_press(key):
    print('{0} pressed'.format(
        key))
    key =str(key).upper()
    s.write(str(key).encode())
def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()