import numpy as np
import cv2
import image_transform

img_1 = cv2.imread("data/images/tiger stare.jpg", cv2.IMREAD_COLOR)

img_2 = cv2.imread("data/images/jaguar stare.jpg", cv2.IMREAD_COLOR)

image_transform.transform_image(img_1, img_2)
