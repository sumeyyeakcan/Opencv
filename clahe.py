import cv2
import numpy as np

def clahe_color(image):
    """Apply CLAHE to a color image."""

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE to the grayscale image
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(grayscale_image)

    # Convert the CLAHE image back to color
    color_image = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2BGR)

    return color_image

# Open the satellite image
image = cv2.imread("rgb.png")

# Apply CLAHE to the image
clahe_image = clahe_color(image)

# Save the CLAHE image
cv2.imwrite("clahe_image1.png", clahe_image)
#calıstı  sıyah beyaz
