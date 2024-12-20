import cv2

# Read the image
image = cv2.imread("C:\\Users\\pc\\Desktop\\sample.jfif")

# Check if the image was successfully loaded
if image is None:
    print("Error: The image file could not be loaded. Please check the file path.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("grayscale_sample.jpg", grayscale_image)

    print("The grayscale image has been saved as 'grayscale_sample.jpg'.")