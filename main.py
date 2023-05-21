import numpy as np
import cv2
import image_transform

def resize_image_proportionally(image, new_width):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the aspect ratio
    ratio = new_width / width

    # Calculate the new height using the aspect ratio
    new_height = int(height * ratio)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image

common_width = 400

img_1 = cv2.imread("data/images/abc test.png", cv2.IMREAD_COLOR)
img_1 = resize_image_proportionally(img_1, common_width)

img_2 = cv2.imread("data/images/abc test flipped.png", cv2.IMREAD_COLOR)
img_2 = resize_image_proportionally(img_2, common_width)

image_transform.run_gui(img_1, img_2)