import cv2
import numpy as np


class Kernel:
    def __init__(self, image, kernel_ratio=30):
        self.kernel_length = np.array(image).shape[1] // kernel_ratio
        self.vertical_kernel = self._get_vertical_kernel()
        self.horizontal_kernel = self._get_horizontal_kernel()

    def _get_vertical_kernel(self):
        return cv2.getStructuringElement(cv2.MORPH_RECT, (1, self.kernel_length))

    def _get_horizontal_kernel(self):
        return cv2.getStructuringElement(cv2.MORPH_RECT, (self.kernel_length, 1))
