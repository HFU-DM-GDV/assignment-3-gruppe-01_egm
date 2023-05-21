import numpy as np
import cv2
from image_transform import guided_image_transform 
from hybrid_imaging import create_hybrid_image

img_1 = cv2.imread("data/images/tiger stare.jpg", cv2.IMREAD_COLOR)

img_2 = cv2.imread("data/images/jaguar stare.jpg", cv2.IMREAD_COLOR)

img_2_transformed = guided_image_transform(img_1, img_2)

create_hybrid_image(img_1, img_2_transformed, 3, 20)

