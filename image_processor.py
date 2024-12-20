import cv2

# Read the image
image = cv2.imread("C:\\Users\\pc\\Desktop\\image_processing_exam\\sample.jfif")

# Check if the image was successfully loaded
if image is None:
    print("Error: The image file could not be loaded. Please check the file path.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("grayscale_sample.jpg", grayscale_image)

    # Resize the image to 100x100 pixels
    resized_image = cv2.resize(grayscale_image, (100, 100))
    cv2.imwrite("resized_sample.jpg", resized_image)

    # Apply a Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(resized_image, (15, 15), 0)
    cv2.imwrite("blurred_sample.jpg", blurred_image)

    print("The grayscale, resized, and blurred images have been saved.")
