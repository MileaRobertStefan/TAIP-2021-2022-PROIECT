from aop import AspectType

from core.detection_facade import DetectionFacade
from time_logging.time_logger import InvocationLoggerAspect
from utils.types import Result


class FaceDetectionService(metaclass=AspectType):
    def __init__(self):
        pass

    @staticmethod
    def get_faces(image):
        faces = DetectionFacade.detect(image)
        return Result(len(faces) > 0, faces)


FaceDetectionService.pointcut('get_faces', InvocationLoggerAspect)
