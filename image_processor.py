import cv2
import matplotlib.pyplot as plt

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
    resized_image = cv2.resize(image, (100, 100))
    cv2.imwrite("resized_sample.jpg", resized_image)

    # Apply a Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite("blurred_sample.jpg", blurred_image)

    # Display the processed images using Matplotlib
    plt.figure(figsize=(10, 5))

    # Original image
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Grayscale image
    plt.subplot(1, 4, 2)
    plt.imshow(grayscale_image, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    # Resized image
    plt.subplot(1, 4, 3)
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title("Resized Image")
    plt.axis("off")

    # Blurred image
    plt.subplot(1, 4, 4)
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.title("Blurred Image")
    plt.axis("off")

    # Show all images
    plt.tight_layout()
    plt.show()

    print("The grayscale, resized, and blurred images have been saved and displayed.")
