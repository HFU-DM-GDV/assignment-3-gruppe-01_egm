
import numpy as np
import cv2

img_m = cv2.imread("data/images/angry_man.png", cv2.IMREAD_COLOR)
img_m = cv2.resize(img_m, (400, 400), interpolation=cv2.INTER_CUBIC)
img_m_copy = img_m.copy()

img_w = cv2.imread("data/images/woman.png", cv2.IMREAD_COLOR)
img_w = cv2.resize(img_w, (400, 400), interpolation=cv2.INTER_CUBIC)
img_w_copy = img_w.copy()


#ksize - kernel size, should be odd and positive (3,5,...)
kernel_size = 21
k_size = (kernel_size, kernel_size)
# sigma - Gaussian standard deviation. If it is non-positive, it is computed from ksize as sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8 
sigma = 0.3*((kernel_size-1)*0.5 - 1) + 0.8 

img_m_copy = cv2.GaussianBlur(img_m_copy,k_size,sigma)

img_w_copy = cv2.GaussianBlur(img_w_copy,k_size,sigma)
img_w_copy = img_w - img_w_copy

img_Ergebnis = img_w_copy + img_m_copy


cv2.namedWindow("Angry_Man")
cv2.namedWindow("Woman")
cv2.namedWindow("Angry_Man_test")
cv2.namedWindow("Woman_test")
cv2.namedWindow("Ergebnis_test")


cv2.imshow("Angry_Man", img_m)
cv2.imshow("Woman", img_w)
cv2.imshow("Angry_Man_test", img_m_copy)
cv2.imshow("Woman_test", img_w_copy)
cv2.imshow("Ergebnis_test", img_Ergebnis)
cv2.waitKey(0)