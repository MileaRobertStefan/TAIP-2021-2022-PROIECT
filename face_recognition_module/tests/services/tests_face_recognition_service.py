import unittest

from services.face_recognition_service import FaceRecognitionService
from tests.test_data.test_data_paths import TestDataPaths


class FaceRecognitionServiceTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_recognition_when_valid_identity(self):

        result = FaceRecognitionService\
            .get_recognized_faces(TestDataPaths.valid_single_identity_path(), TestDataPaths.image_path())

        self.assertTrue(result.has_faces)
        self.assertEqual(1, len(result.coordinates))

    def test_recognition_when_invalid_identity(self):

        result = FaceRecognitionService\
            .get_recognized_faces(TestDataPaths.tyler1_identity_path(), TestDataPaths.image_path())

        self.assertFalse(result.has_faces)
        self.assertEqual(0, len(result.coordinates))
