import cv2


class MorphologicalOperation:
    def __init__(self, binary_image, kernel):
        self.binary_image = binary_image
        self.kernel = kernel

    def detect_vertical_lines(self):
        img_temp1 = cv2.erode(self.binary_image, self.kernel.vertical_kernel, iterations=3)
        return cv2.dilate(img_temp1, self.kernel.vertical_kernel, iterations=3)

    def detect_horizontal_lines(self):
        img_temp2 = cv2.erode(self.binary_image, self.kernel.horizontal_kernel, iterations=3)
        return cv2.dilate(img_temp2, self.kernel.horizontal_kernel, iterations=3)
