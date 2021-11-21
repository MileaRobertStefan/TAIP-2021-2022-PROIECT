import types


# facade design pattern
class FaceDetectionController:
    def __init__(self, image_decryption_service, face_detection_service):
        self.image_decryption_service = image_decryption_service
        self.face_detection_service = face_detection_service

    def detect_faces(self, http_request):
        # uses image_decryption_service to decrypt the image, then face_detection_service
        # to detect the faces
        pass


# builder design pattern
class ServiceBuilder:
    def getService(self): pass


class ImageDecryptionServiceBuilder(ServiceBuilder):
    def getService(self):
        # build image decryption service
        pass


class FaceDetectionServiceBuilder(ServiceBuilder):
    def getService(self):
        # build face detection service
        pass


# strategy design pattern
class ImageDecryptionService:
    def __init__(self, pfx_service, decrypt_function=None):
        self.pfx_service = pfx_service
        if decrypt_function is not None:
            self.decrypt_image = types.MethodType(decrypt_function, self)

    def decrypt_image(self, image):
        pass


# singleton design pattern
class PfxService:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if PfxService.__instance is None:
            PfxService()
        return PfxService.__instance

    def __init__(self):
        if PfxService.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PfxService.__instance = self

    def __generate_keys(self):
        pass

    def __generate_certificate(self):
        pass


class FaceDetectionService:
    def __init__(self, face_detection_model):
        self.face_detection_model = face_detection_model

    def get_faces(self, image):
        pass


class FaceDetectionResult:
    def __init__(self, has_faces, coordinates):
        self.has_faces = has_faces
        self.coordinates = coordinates

    def has_faces(self, has_faces):
        pass

    def set_coordinates(self, coordinates):
        pass


class RectangleCoordinates:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right


class FaceDetectionModel:
    def __init__(self, model):
        self.model = model

    def get_faces(self, image):
        pass

    def preprocess(self, image):
        pass
