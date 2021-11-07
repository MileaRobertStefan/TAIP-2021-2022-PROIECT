from core.detection_facade import DetectionFacade
from utils.types import Result


class FaceDetectionService:
    def __init__(self):
        pass

    @staticmethod
    def get_faces(image):
        faces = DetectionFacade.detect(image)
        return Result(len(faces) > 0, faces)
