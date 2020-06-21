import cv2
import imutils

class Contours:
    def __init__(self, blurred_image):
        self.blurred_image = blurred_image
        self.edged_image = cv2.Canny(self.blurred_image, 75, 200)

    def find_screen_contour(self):
        contours = self.find_contours()
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                return approx

    def find_contours(self):
        contours = cv2.findContours(self.edged_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        return sorted(contours, key=cv2.contourArea, reverse=True)[:5]