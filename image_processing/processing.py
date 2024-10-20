import cv2
import numpy as np

def read_image(file_path):
    """Reads an image from a file path."""
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"Image file '{file_path}' not found.")
    return image

def save_image(file_path, image):
    """Saves an image to a file path."""
    cv2.imwrite(file_path, image)

def resize_image(image, width, height):
    """Resizes an image to the given width and height."""
    return cv2.resize(image, (width, height))

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image, kernel_size):
    """Applies a Gaussian blur to the image."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
