import cv2
import numpy as np

def clahe_unsharp_masking(image):
  # Convert the image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply CLAHE to the grayscale image
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  enhanced_image = clahe.apply(gray_image)

  # Apply unsharp masking to the enhanced image
  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
  unsharp_image = cv2.filter2D(enhanced_image, -1, kernel)

  # Return the unsharp masked image
  return unsharp_image

if __name__ == "__main__":
  # Read the color satellite image
  image = cv2.imread("rgb.png")

  # Apply CLAHE and unsharp masking to the image
  enhanced_image = clahe_unsharp_masking(image)

  # Show the original and enhanced images
  cv2.imshow("Original Image", image)
  cv2.imshow("Enhanced Image", enhanced_image)
 
  cv2.waitKey(0)
  cv2.imwrite(enhanced_image)
  #calısıyor ve emhanced_image.png dıye kaydettım
