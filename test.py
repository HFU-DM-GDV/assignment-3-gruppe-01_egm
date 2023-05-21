import cv2
from pynput import keyboard

img = cv2.imread("data/images/tiger stare.jpg", cv2.IMREAD_COLOR)


# def on_press(key):

#     keyboard.press('a')
#     keyboard.release('a')

# listener = keyboard.Listener(on_press=lambda key: on_press(key))
# listener.start()

cv2.imshow("title", img)
key = cv2.waitKey(0)

if key == keyboard.Key.up:
    print("up")

if key == ord('a'):
    print("a")
