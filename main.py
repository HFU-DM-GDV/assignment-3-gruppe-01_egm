import cv2
from image_transform import guided_image_transform 
from hybrid_imaging import create_hybrid_image

# Import images
img_1 = cv2.imread("data/images/jaguar stare.jpg", cv2.IMREAD_COLOR)
img_2 = cv2.imread("data/images/dog stare.jpg", cv2.IMREAD_COLOR)

# Transform the second image
img_2_transformed = guided_image_transform(img_1, img_2)

# Specify cutoff frequency parameters
cutoff_frequency_1 = 10
cutoff_frequency_2 = 13

# Create hybrid image from img_1 and the transformed img_2 with separate cutoff frequencies
create_hybrid_image(img_1, img_2_transformed, cutoff_frequency_1, cutoff_frequency_2)
