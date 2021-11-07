class Result:
    def __init__(self, has_faces, coordinates):
        self.has_faces = has_faces
        self.coordinates = coordinates


class FaceCoordinates:
    def __init__(self, coordinates):
        self.top, self.right, self.bottom, self.left = coordinates

    def get_list(self):
        return self.top, self.right, self.bottom, self.left
