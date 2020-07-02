import cv2
import imutils


class ImageAdapter:
    def __init__(self, image_cv2_object):
        self.image_cv2_object = image_cv2_object.copy()
        self.scaled_ratio, self.downscaled_image = self.downscale_image()
        self.image_edges = self.find_edges()

    def downscale_image(self):
        downscaled_height = 500
        scaled_ratio = self.image_cv2_object.shape[0] / downscaled_height
        downscaled_image = imutils.resize(self.image_cv2_object, height=downscaled_height)
        return scaled_ratio, downscaled_image

    def find_edges(self):
        gray_image = cv2.cvtColor(self.downscaled_image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        return cv2.Canny(blurred_image, 75, 200)

