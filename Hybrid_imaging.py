
import numpy as np
import cv2

img_m = cv2.imread("data/images/angry_man.png", cv2.IMREAD_COLOR)
img_m = cv2.resize(img_m, (400, 400))

img_w = cv2.imread("data/images/woman.png", cv2.IMREAD_COLOR)
img_w = cv2.resize(img_w, (400, 400))

cutoff_frequency = 10

img_m_low = cv2.GaussianBlur(img_m,(0,0), cutoff_frequency)

img_w_high = cv2.subtract(img_w, cv2.GaussianBlur(img_w,(0,0), cutoff_frequency))

img_Ergebnis = cv2.add(img_m_low, img_w_high)


cv2.namedWindow("Angry_Man")
cv2.namedWindow("Woman")
cv2.namedWindow("Angry_Man_test")
cv2.namedWindow("Woman_test")
cv2.namedWindow("Ergebnis_test", cv2.WINDOW_FREERATIO)


cv2.imshow("Angry_Man", img_m)
cv2.imshow("Woman", img_w)
cv2.imshow("Angry_Man_test", img_m_low)
cv2.imshow("Woman_test", img_w_high)
cv2.imshow("Ergebnis_test", img_Ergebnis)
cv2.waitKey(0)