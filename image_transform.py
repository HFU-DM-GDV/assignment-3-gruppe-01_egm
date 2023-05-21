import numpy as np
import cv2

# Define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []


def click_src(event, x, y, flags, original):
    # Grab references to the global variables
    global ref_pt_src

    # If the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_src)
        if pos == 0:
            ref_pt_src = [(x, y)]
        else:
            ref_pt_src.append((x, y))
        # Draw a circle around the clicked point
        cv2.circle(original, ref_pt_src[pos], 4, (0, 255, 0), 2)
        cv2.imshow("Master Image", original)


def click_dst(event, x, y, flags, transformed):
    # Grab references to the global variables
    global ref_pt_dst

    # If the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_dst)
        if pos == 0:
            ref_pt_dst = [(x, y)]
        else:
            ref_pt_dst.append((x, y))
        # Draw a circle around the clicked point
        cv2.circle(transformed, ref_pt_dst[pos], 4, (0, 255, 0), 2)
        cv2.imshow("Transformee image", transformed)

def run_gui(master_img, transformee_img):
    
    global ref_pt_src
    global ref_pt_dst

    # Initialize needed variables and windows
    rows, cols, dim = master_img.shape
    clone = master_img.copy()
    dst_transform = np.zeros(transformee_img.shape, np.uint8)

    cv2.namedWindow("Master Image")
    cv2.setMouseCallback("Master Image", click_src, master_img)
    cv2.namedWindow("Transformee image")
    cv2.setMouseCallback("Transformee image", click_dst, transformee_img)
    cv2.namedWindow("Result")

    # Keep looping until the 'q' key is pressed
    computationDone = False
    while True:
        # If there are three reference points, then compute the transform and apply the transformation
        if not (computationDone) and (len(ref_pt_src) == 3 and len(ref_pt_dst) == 3):
            T_affine = cv2.getAffineTransform(np.float32(ref_pt_src), np.float32(ref_pt_dst))

            print("\nAffine transformation:\n",
                "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_affine]))

            dst_transform = cv2.warpAffine(transformee_img, T_affine, (cols, rows))
            computationDone = True

        # Display the image and wait for a keypress
        cv2.imshow("Master Image", master_img)
        cv2.imshow("Transformee image", transformee_img)
        cv2.imshow("Result", dst_transform)

        key = cv2.waitKey(10)
        # If the 'r' key is pressed, reset the transformation
        if key == ord("r"):
            dst_transform = np.zeros(transformee_img.shape, np.uint8)
            master_img = clone.copy()
            ref_pt_src = []
            ref_pt_dst = []
            computationDone = False
        # If the 'q' key is pressed, break from the loop
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()
