import cv2
import json
from .patch import Patch


class ImageAdapter:
    def __init__(self, image_cv2_object, patch_data_path):
        self.patch_data_path = patch_data_path
        self.width = int(image_cv2_object.shape[1])
        self.height = int(image_cv2_object.shape[0])
        self.image_cv2_object = image_cv2_object

    def get_binary_image(self):
        grayed_image = cv2.cvtColor(self.image_cv2_object, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayed_image, (5, 5), 0)
        (thresh, img_bin) = cv2.threshold(blurred_image, 80, 255, cv2.THRESH_BINARY)
        return 255 - img_bin

    def strip_sides_of_image(self, horizontal_frame_points):
        s = 0
        for w in range(1, self.width):
            if horizontal_frame_points[w] == 255 and horizontal_frame_points[w - 1] == 0:
                s = w
            if horizontal_frame_points[w] == 0 and horizontal_frame_points[w - 1] == 255:
                if s != 0:
                    self.image_cv2_object = self.image_cv2_object[:, s:w]

    def extract_patches(self, vertical_frame_points):
        with open(self.patch_data_path) as json_file:
            data = json.load(json_file)
        patches = []
        count = 1
        s = 0
        for h in range(1, self.height):
            if count == 9:
                break
            if vertical_frame_points[h] == 255 and vertical_frame_points[h - 1] == 0:
                s = h
            if vertical_frame_points[h] == 0 and vertical_frame_points[h - 1] == 255:
                if s != 0:
                    patches.append(Patch(self.image_cv2_object[s:h, :], data[str(count)]))
                    count += 1
        return patches
