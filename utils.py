import cv2

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