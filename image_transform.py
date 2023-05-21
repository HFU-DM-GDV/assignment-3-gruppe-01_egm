import numpy as np
import cv2
from utils import resize_image_proportionally

# Define global arrays for the clicked (reference) points
__ref_pt_original = []
__ref_pt_transformed = []

def __click_src(event, x, y, flags, original):
    # Grab references to the global variables
    global __ref_pt_original

    # If the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(__ref_pt_original)
        if pos == 0:
            __ref_pt_original = [(x, y)]
        else:
            __ref_pt_original.append((x, y))
        # Draw a circle around the clicked point
        cv2.circle(original, __ref_pt_original[pos], 4, (0, 255, 0), 2)
        cv2.imshow("Master image", original)


def __click_dst(event, x, y, flags, transformee):
    # Grab references to the global variables
    global __ref_pt_transformed

    # If the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(__ref_pt_transformed)
        if pos == 0:
            __ref_pt_transformed = [(x, y)]
        else:
            __ref_pt_transformed.append((x, y))
        # Draw a circle around the clicked point
        cv2.circle(transformee, __ref_pt_transformed[pos], 4, (0, 255, 0), 2)
        cv2.imshow("Transformee image", transformee)

def transform_image(master_img, transformee_img):
    '''Will guide the user in transforming the transformee image to match the master image'''
    
    print("Transforming one of the images to more closely match the other can result in a more interesting effect.\n")
    choice = input("Would you like to go through a guided transformation to achieve this? (y/n)\n")
    if choice == 'n':
          return transformee_img
    if choice != 'y':
          print("Invalid input. Defaulting to 'no'.")
          return transformee_img
    
    print("\nClick on three points in the transformee image. These should be distinct features that are also present in the master image.\n"
          "These points should be selected in the same order in both images or one by one in alternating fashion.\n"
          "'r' to reset the points\n"
          "'q' to quit when you are happy with the transformed image\n")

    master_img = resize_image_proportionally(master_img, 400)
    transformee_img = resize_image_proportionally(transformee_img, 400)

    global __ref_pt_original
    global __ref_pt_transformed

    # Initialize needed variables and windows
    rows, cols, dim = master_img.shape
    transformee_img_clean = transformee_img.copy()
    master_img_clean = master_img.copy()
    dst_transform = np.zeros(transformee_img.shape, np.uint8)

    cv2.namedWindow("Master image")
    cv2.setMouseCallback("Master image", __click_src, master_img)
    cv2.namedWindow("Transformee image")
    cv2.setMouseCallback("Transformee image", __click_dst, transformee_img)
    cv2.namedWindow("Transformed image")

    # Keep looping until the 'q' key is pressed
    computationDone = False
    while True:
        # If there are three reference points, then compute the transform and apply the transformation
        if not (computationDone) and (len(__ref_pt_original) == 3 and len(__ref_pt_transformed) == 3):
            T_affine = cv2.getAffineTransform(np.float32(__ref_pt_transformed), np.float32(__ref_pt_original))

            print("\nAffine transformation:\n",
                "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_affine]))

            dst_transform = cv2.warpAffine(transformee_img_clean, T_affine, (cols, rows))
            computationDone = True

        # Display the image and wait for a keypress
        cv2.imshow("Master image", master_img)
        cv2.imshow("Transformee image", transformee_img)
        cv2.imshow("Transformed image", dst_transform)

        key = cv2.waitKey(10)
        # If the 'r' key is pressed, reset the transformation
        if key == ord("r"):
            dst_transform = np.zeros(transformee_img_clean.shape, np.uint8)
            master_img = master_img_clean.copy()
            transformee_img = transformee_img_clean.copy()
            __ref_pt_original = []
            __ref_pt_transformed = []
            computationDone = False
            cv2.setMouseCallback("Master image", __click_src, master_img)
            cv2.setMouseCallback("Transformee image", __click_dst, transformee_img)
        # If the 'q' key is pressed, break from the loop
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()
    
    # return the transformed image if the computation was executed
    if computationDone:
        print("Returned non-transformed image.")
        return dst_transform
    
    print("Returned transformed image.")
    return transformee_img