import unittest
import sys, os
from mock import MagicMock
import json

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), "../")
)
from main.annotator import Annotator


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        json_contents = '''
        [{
            "annotation_class": "phase1",
            "id": "30",
            "name": "Outside Over Garage Lights",
            "time": [
                "1350939543.43",
                "1350939603.43"
            ]
        }, {
            "annotation_class": "phase2",
            "id": "30",
            "name": "Outside Over Garage Lights",
            "time": [
                "1350939662.29",
                "1350939722.29"
            ]
        }]'''

        self.annotator = Annotator()
        self.annotator.read_json_file = MagicMock(return_value=json.loads(json_contents))

    def test_get_annotations_from_json(self):
        annotations = self.annotator.get_annotations_from_json("/dummy/file/location")
        self.assertEquals(annotations["annotation_class"][0],"phase1")
        self.assertEquals(annotations["id"][1],"30")
        self.assertEquals(annotations["name"][0],"Outside Over Garage Lights")
        self.assertEquals(annotations["time"][1][0],"1350939662.29")

if __name__ == '__main__':
    unittest.main()