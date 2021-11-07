from core.recognition_facade import RecognitionFacade
from utils.types import Result


class FaceRecognitionService:
    def __init__(self):
        pass

    @staticmethod
    def get_faces(identity_image, image):
        faces = RecognitionFacade.detect(identity_image, image)
        return Result(len(faces) > 0, faces)
