import cv2
import numpy as np

def image_blur(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Invert the blurred image
    inverted = cv2.bitwise_not(blurred)

    # Apply the pencil sketch effect
    sketch = cv2.divide(gray, inverted, scale=256.0)

    # Save the sketch image
    cv2.imwrite('image_blur.jpg', sketch)

input_image_path = 'img.jpg'
output_image_path = 'image_blur.jpg'
image_blur(input_image_path, output_image_path)