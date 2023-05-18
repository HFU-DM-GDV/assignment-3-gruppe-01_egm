
import numpy as np
import cv2

img_1 = cv2.imread("data/images/angry_man.png", cv2.IMREAD_COLOR)
img_1 = cv2.resize(img_1, (400, 400))

img_2 = cv2.imread("data/images/woman.png", cv2.IMREAD_COLOR)
img_2 = cv2.resize(img_2, (400, 400))

cutoff_frequency_low = 5
cutoff_frequency_high = 10

def lowpass (img, cutoff_frequency):
    return cv2.GaussianBlur(img,(0,0), cutoff_frequency)

def highpass (img, cutoff_frequency):
    return cv2.subtract(img, cv2.GaussianBlur(img,(0,0), cutoff_frequency))

def hybrid_image (img1,img2):
    return cv2.add(lowpass(img1,cutoff_frequency_low), highpass(img2,cutoff_frequency_high))

img_result = hybrid_image(img_1,img_2)

img_result_big = cv2.resize(img_result, (800, 800))
img_result_small = cv2.resize(img_result, (150, 150))


cv2.namedWindow("Result_big")
cv2.namedWindow("Result_small")

cv2.imshow("Result_big", img_result_big)
cv2.imshow("Result_small", img_result_small)
cv2.waitKey(0)