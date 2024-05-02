import cv2 

def process_image_opencv(crop_start, image_path, crop_end, padding, end_size):
    """
    Processes an image with cropping, padding, and resizing using OpenCV.

    Args:
        crop_start (tuple): (x, y) coordinates of the top-left corner of the crop area.
        image_path (str): Path to the image file.
        crop_end (tuple): (x, y) coordinates of the bottom-right corner of the crop area.
        padding (tuple): (top, bottom, left, right) padding values.
        end_size (tuple): (x, y) desired output image size.

    Returns:
        numpy.ndarray: The processed image.
    """

    try:
        image = cv2.imread(image_path)

        # Cropping
        cropped_image = image[crop_start[1]:crop_end[1], crop_start[0]:crop_end[0]]

        # Padding (OpenCV requires border type)
        padded_image = cv2.copyMakeBorder(cropped_image, 
                                          top=padding[0], bottom=padding[1], 
                                          left=padding[2], right=padding[3],
                                          borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])

        # Resizing if necessary
        if padded_image.shape[:2] != end_size:
            resized_image = cv2.resize(padded_image, end_size, interpolation=cv2.INTER_AREA) 
        else:
            resized_image = padded_image

        return resized_image

    except Exception as e:  # Basic exception handling
        print(f"An error occurred: {e}")
        return None
    

# Test the function
# crop_start = (128, 36)
# crop_end = (896, 708)
# padding = (64, 64, 16, 16)
# end_size = (256, 256)
# base_dir = "/home/ark/Documents/Ultrasound Guided Needle Project/needle segmentation_modified/SH00006/SH000060000.png"
# cv2.imshow("Original Image", cv2.imread(base_dir))
# cv2.imshow("Processed Image", process_image_opencv(crop_start, base_dir, crop_end, padding, end_size))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
