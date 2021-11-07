import cv2
import face_recognition

from services.face_recognition_service import FaceRecognitionService


def load_image(path):
    return face_recognition.load_image_file(path)


if __name__ == '__main__':
    image = load_image("photo.jpg")
    identity = load_image("identity.jpg")
    result = FaceRecognitionService.get_faces(identity_image=identity, image=image)
    if result.has_faces:
        for index, coord in enumerate(result.coordinates):
            face_image = image[coord.top:coord.bottom, coord.left:coord.right]
            cv2.imshow(str(index), face_image)

    cv2.waitKey(0)
