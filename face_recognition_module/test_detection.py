import cv2
import face_recognition

from services.face_detection_service import FaceDetectionService


def load_image():
    return face_recognition.load_image_file("photo.jpg")


if __name__ == '__main__':
    image = load_image()
    result = FaceDetectionService.get_faces("photo.jpg")
    if result.has_faces:
        for index, coord in enumerate(result.coordinates):
            face_image = image[coord.top:coord.bottom, coord.left:coord.right]
            cv2.imshow(str(index), face_image)

    cv2.waitKey(0)
