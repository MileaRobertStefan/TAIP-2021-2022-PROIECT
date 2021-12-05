import unittest
import face_recognition

from core.recognition_facade import RecognitionFacade
from tests.test_data.test_data_paths import TestDataPaths


class RecognitionFacadeTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_detect_when_valid_identity(self):
        identity = face_recognition.load_image_file(TestDataPaths.valid_single_identity_path())
        image = face_recognition.load_image_file(TestDataPaths.image_path())

        result = RecognitionFacade.detect(identity, image)

        self.assertEqual(1, len(result))

    def test_detect_when_invalid_identity(self):
        identity = face_recognition.load_image_file(TestDataPaths.tyler1_identity_path())
        image = face_recognition.load_image_file(TestDataPaths.image_path())

        result = RecognitionFacade.detect(identity, image)

        self.assertEqual(0, len(result))

