import face_recognition

from utils.types import FaceCoordinates


class RecognitionFacade:
    def __init__(self):
        pass

    @staticmethod
    def detect(identity_image, image):
        face_locations = face_recognition.face_locations(image)
        identity_locations = face_recognition.face_locations(identity_image)
        if len(face_locations) == 0 or len(identity_locations) == 0:
            return face_locations
        faces_encoding = face_recognition.face_encodings(image, face_locations)
        identity_encoding = face_recognition.face_encodings(identity_image, identity_locations)
        known_faces_coordinates = []
        for index, encoding in enumerate(faces_encoding):
            result = face_recognition.compare_faces(identity_encoding, encoding)
            if result.__contains__(True):
                known_faces_coordinates.append(face_locations[index])
        return [FaceCoordinates(coordinates) for coordinates in known_faces_coordinates]





