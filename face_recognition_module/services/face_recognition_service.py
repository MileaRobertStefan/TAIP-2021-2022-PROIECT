from aop import AspectType

from core.recognition_facade import RecognitionFacade
from time_logging.time_logger import InvocationLoggerAspect
from utils.types import Result


class FaceRecognitionService(metaclass=AspectType):
    def __init__(self):
        pass

    @staticmethod
    def get_recognized_faces(identity_image, image):
        faces = RecognitionFacade.detect(identity_image, image)
        return Result(len(faces) > 0, faces)


FaceRecognitionService.pointcut('get_recognized_faces', InvocationLoggerAspect)
