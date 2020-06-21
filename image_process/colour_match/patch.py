import cv2
import numpy as np
from skimage.color import rgb2lab, deltaE_cie76
from .color_code_converter import hex_to_rgb
from .color_code_converter import rgb_to_hex

class Patch:
    def __init__(self, patch, data):
        self.patch_color = self._get_colors(patch)
        self.name = data["name"]
        self.corresponding_block_data = data["color_blocks"]

    def get_matched_color(self):
        val = 999999
        col = ''
        for key, value in self.corresponding_block_data.items():
            diff = self._match_patch_color(value)
            if diff < val:
                val = diff
                col = key
        return col

    def _match_patch_color(self, color):
        selected_color = rgb2lab(np.uint8(np.asarray([[hex_to_rgb(color)]])))
        patch_color = rgb2lab(np.uint8(np.asarray([[hex_to_rgb(self.patch_color)]])))
        diff = deltaE_cie76(selected_color, patch_color)
        return diff

    @staticmethod
    def _get_colors(patch):
        b, g, r = cv2.split(patch)
        [r_, g_, b_] = [np.mean(r, dtype=np.int), np.mean(g, dtype=np.int), np.mean(b, dtype=np.int)]
        return rgb_to_hex(r_, g_, b_).upper()
