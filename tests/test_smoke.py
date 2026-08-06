import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ModelWorkflowTests(unittest.TestCase):
    def test_training_and_prediction_smoke(self):
        train = subprocess.run(
            [sys.executable, "src/train.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(train.returncode, 0, msg=train.stderr or train.stdout)

        model_path = ROOT / "model" / "student_model.pkl"
        self.assertTrue(model_path.exists(), f"Expected model at {model_path}")

        predict = subprocess.run(
            [sys.executable, "src/predict.py"],
            input="6\n72.6\n7\n",
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(predict.returncode, 0, msg=predict.stderr or predict.stdout)
        self.assertIn("Prediction:", predict.stdout)


if __name__ == "__main__":
    unittest.main()
