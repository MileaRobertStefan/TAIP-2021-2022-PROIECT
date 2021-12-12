import unittest

from services.face_detection_service import FaceDetectionService
from tests.test_data.test_data_paths import TestDataPaths


class FaceDetectionTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_detect_when_multiple_identities(self):

        result = FaceDetectionService.get_faces(TestDataPaths.image_path())

        self.assertTrue(result.has_faces)
        self.assertEqual(5, len(result.coordinates))

    def test_detect_when_single_identity(self):

        result = FaceDetectionService.get_faces(TestDataPaths.tyler1_identity_path())

        self.assertTrue(result.has_faces)
        self.assertEqual(1, len(result.coordinates))

    def test_detect_when_no_face_present(self):

        result = FaceDetectionService.get_faces(TestDataPaths.no_identity_path())

        self.assertFalse(result.has_faces)
        self.assertEqual(0, len(result.coordinates))
