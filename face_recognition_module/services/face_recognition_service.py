import face_recognition
from aop import AspectType

from core.recognition_facade import RecognitionFacade
from utils.types import Result


class FaceRecognitionService(metaclass=AspectType):
    def __init__(self):
        pass

    @staticmethod
    def get_recognized_faces(identity_path, image_path):
        image = face_recognition.load_image_file(image_path)
        identity = face_recognition.load_image_file(identity_path)

        faces = RecognitionFacade.detect(identity, image)

        return Result(len(faces) > 0, faces)
