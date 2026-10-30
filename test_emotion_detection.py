import json
import unittest

from emotion_detection import emotion_detector


def dominant(text):
    """Return the emotion with the highest score for the given text."""
    result = json.loads(emotion_detector(text))
    emotions = result["emotionPredictions"][0]["emotion"]
    return max(emotions, key=emotions.get)


class TestEmotionDetector(unittest.TestCase):
    """Basic tests for the emotion_detector function."""

    def test_joy(self):
        """Joy statement is detected as joy."""
        self.assertEqual(dominant("I am glad this happened"), "joy")

    def test_anger(self):
        """Anger statement is detected as anger."""
        self.assertEqual(dominant("I am really mad about this"), "anger")


if __name__ == "__main__":
    unittest.main()
