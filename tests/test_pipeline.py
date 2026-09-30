import unittest
from pathlib import Path

from optic_sorter.pipeline import analyze


class PipelineTest(unittest.TestCase):
    def test_detects_parts_and_actions(self):
        sample = Path(__file__).parents[1] / "samples" / "workcell.ppm"
        result = analyze(sample)
        labels = {item["label"] for item in result["detections"]}
        self.assertTrue({"red_part", "blue_part", "green_bin", "yellow_hazard"} <= labels)
        self.assertTrue(any(action["action"] == "pick" for action in result["pick_list"]))


if __name__ == "__main__":
    unittest.main()
