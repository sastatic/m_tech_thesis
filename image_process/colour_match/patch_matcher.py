import cv2
from image_process.colour_match.image_adapter import ImageAdapter
from .morphological_operation import MorphologicalOperation
from .kernel import Kernel
from .image_frame_points import ImageFramePoints

class PatchMatcher:
	def __init__(self, image_path, patch_data_path):
		self.image_cv2_object = cv2.imread(image_path)
		self.patch_data_path = patch_data_path
		self.patches = None

	def patch_extract(self):
		img_adapter = ImageAdapter(self.image_cv2_object, self.patch_data_path)
		kernel = Kernel(self.image_cv2_object)
		morphological_operation = MorphologicalOperation(img_adapter.get_binary_image(), kernel)
		img_frame_points = ImageFramePoints(morphological_operation)
		img_adapter.strip_sides_of_image(img_frame_points.horizontal_frame_points)
		self.patches = img_adapter.extract_patches(img_frame_points.vertical_frame_points)
		return self._get_strip_information()

	def _get_strip_information(self):
		matches = {}
		for patch in self.patches:
			matches[patch.name] = patch.get_matched_color()
		return matches
