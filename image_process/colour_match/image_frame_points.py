class ImageFramePoints:
    def __init__(self, morphological_operation):
        self.vertical_lines_img = morphological_operation.detect_vertical_lines()
        self.horizontal_lines_img = morphological_operation.detect_horizontal_lines()
        self.image_width = morphological_operation.binary_image.shape[1]
        self.image_height = morphological_operation.binary_image.shape[0]
        self.horizontal_frame_points, self.h_s, self.h_e = self.get_horizontal_frame_points()
        self.vertical_frame_points, self.v_s, self.v_e = self.get_vertical_frame_points(self.h_s, self.h_e)

    def get_horizontal_frame_points(self):
        points = [255] * self.image_width
        for h in range(self.image_height):
            for w in range(self.image_width):
                if self.vertical_lines_img[h][w] == 255:
                    points[w] = 0
        return self._trim_frame_points(points)

    def get_vertical_frame_points(self, starts, ends):
        points = [255] * self.image_height
        for h in range(self.image_height):
            for w in range(starts, ends):
                if self.horizontal_lines_img[h][w] == 255:
                    points[h] = 0
        return self._trim_frame_points(points)

    @staticmethod
    def _trim_frame_points(points):
        starts = 0
        ends = len(points) - 1
        while points[starts] == 0:
            points[starts] = 255
            starts += 1
        while points[ends] == 0:
            points[ends] = 255
            ends -= 1
        return points, starts, ends
