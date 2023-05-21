
import numpy as np
import cv2

def create_hybrid_image(img_1, img_2, cutoff_freq_img_1, cutoff_freq_img_2):
    '''Generate and show a hybrid image from img_1 and img_2.
    img_1 is being filtered by a low-pass filter using cutoff_frequency_1 and
    img_2 is being filtered by a high-pass filter using cutoff_frequency_2'''

    # Ensure the images are of equal size
    img_2 = cv2.resize(img_2, (img_1.shape[1], img_1.shape[0]))

    img_result = hybrid_image(img_1, img_2, cutoff_freq_img_1, cutoff_freq_img_2)

    img_result_big = cv2.resize(img_result, (800, 800))
    img_result_small = cv2.resize(img_result, (150, 150))


    cv2.namedWindow("Result_big")
    cv2.namedWindow("Result_small")

    cv2.imshow("Result_big", img_result_big)
    cv2.imshow("Result_small", img_result_small)
    cv2.waitKey(0)

def lowpass (img, cutoff_frequency):
    '''Return image filtered by low-pass filter'''
    return cv2.GaussianBlur(img,(0,0), cutoff_frequency)

def highpass (img, cutoff_frequency):
    '''Return image filtered by high-pass filter'''
    return cv2.subtract(img, cv2.GaussianBlur(img,(0,0), cutoff_frequency))

def hybrid_image (img_1, img_2, cutoff_frequency_1, cutoff_frequency_2):
    '''Combine filtered images to one hybrid image'''
    return cv2.add(lowpass(img_1, cutoff_frequency_1), highpass(img_2, cutoff_frequency_2))

