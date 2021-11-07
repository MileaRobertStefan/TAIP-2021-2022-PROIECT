import face_recognition

from services.face_detection_service import FaceDetectionService


def load_image():
    return face_recognition.load_image_file("photo.jpg")


if __name__ == '__main__':
    image = load_image()
    coordinates = FaceDetectionService().get_faces(image)
    hello = 0
