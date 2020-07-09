import cv2
import numpy as np
from numpy.linalg import norm as dist
from .image_adapter import ImageAdapter
from .contour import Contours


class ImageTransformer:
	def __init__(self, image_path, max_width, max_height):
		self.image_path = image_path
		self.image_cv2_object = cv2.imread(self.image_path)
		self.max_width, self.max_height = max_width, max_height

	def transform(self):
		img_adapter = ImageAdapter(self.image_cv2_object)
		contours = Contours(img_adapter.image_edges)
		screen_contour_points = contours.find_screen_contour()
		warped = self._four_point_transform(screen_contour_points.reshape(4, 2) * img_adapter.scaled_ratio)
		cv2.imwrite(self.image_path, warped)
		del contours
		del img_adapter

	def _four_point_transform(self, pts):
		rect = self._get_perspective_transformation_points(pts)
		dst = np.float32([[0, 0], [self.max_width, 0], [0, self.max_height], [self.max_width, self.max_height]])
		m = cv2.getPerspectiveTransform(rect, dst)
		warped = cv2.warpPerspective(self.image_cv2_object, m, (self.max_width, self.max_height))
		return warped

	def _get_perspective_transformation_points(self, pts):
		_sum = np.sum(pts, axis=1)
		_dif = np.diff(pts, axis=1)
		rect = np.zeros((4, 2), dtype="float32")
		rect[0] = pts[np.argmin(_sum)]
		rect[1] = pts[np.argmin(_dif)]
		rect[2] = pts[np.argmax(_dif)]
		rect[3] = pts[np.argmax(_sum)]
		if dist(rect[0] - rect[1]) > dist(rect[0] - rect[3]):
			rect[3], rect[0], rect[1], rect[2] = rect[0], rect[1], rect[2], rect[3]
		return rect
