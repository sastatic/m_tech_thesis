from image_process.transformation.image_transformer import ImageTransformer
from image_process.colour_match.patch_matcher import PatchMatcher


class Service:
    def __init__(self, image_path, patch_data_path):
        self.image_path = image_path
        self.patch_data_path = patch_data_path
        self.max_width = 300
        self.max_height = 935

    def main(self):
        self._transform_image()
        return self._match_color()

    def _transform_image(self):
        image_transformer = ImageTransformer(self.image_path, self.max_width, self.max_height)
        image_transformer.transform()
        del image_transformer

    def _match_color(self):
        patch_matcher = PatchMatcher(self.image_path, self.patch_data_path)
        strip_info = patch_matcher.patch_extract()
        del patch_matcher
        return strip_info
