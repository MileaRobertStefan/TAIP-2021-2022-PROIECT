import face_recognition

from utils.types import FaceCoordinates


class DetectionFacade:
    def __init__(self):
        pass

    @staticmethod
    def detect(image):
        faces = face_recognition.face_locations(image)
        return [FaceCoordinates(face) for face in faces]
