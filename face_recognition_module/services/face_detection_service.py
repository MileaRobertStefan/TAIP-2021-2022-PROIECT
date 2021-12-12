import face_recognition
from aop import AspectType

from core.detection_facade import DetectionFacade
from mop.mop_decorators import requires_file_created_before, requires_file_deleted_after, requires_called_before, \
    requires_calls
from utils.types import Result


class FaceDetectionService(metaclass=AspectType):
    def __init__(self):
        pass

    @staticmethod
    @requires_called_before(event_name="save_image")
    @requires_file_created_before
    @requires_file_deleted_after
    @requires_calls(event_name="delete_image")
    def get_faces(path):
        image = face_recognition.load_image_file(path)
        faces = DetectionFacade.detect(image)
        return Result(len(faces) > 0, faces)
