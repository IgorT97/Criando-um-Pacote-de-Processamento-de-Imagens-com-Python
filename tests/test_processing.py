import unittest
import cv2
from image_processing import read_image, save_image, resize_image, convert_to_grayscale, blur_image

class TestImageProcessing(unittest.TestCase):

    def setUp(self):
        self.image_path = 'test_image.jpg'
        self.image = read_image(self.image_path)

    def test_read_image(self):
        image = read_image(self.image_path)
        self.assertIsNotNone(image)

    def test_resize_image(self):
        resized_image = resize_image(self.image, 100, 100)
        self.assertEqual(resized_image.shape[0], 100)
        self.assertEqual(resized_image.shape[1], 100)

    def test_convert_to_grayscale(self):
        gray_image = convert_to_grayscale(self.image)
        self.assertEqual(len(gray_image.shape), 2)

    def test_blur_image(self):
        blurred_image = blur_image(self.image, 5)
        self.assertIsNotNone(blurred_image)

if __name__ == '__main__':
    unittest.main()
