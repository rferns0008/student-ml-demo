from joblib import load
from pathlib import Path
import pandas as pd
import sys


def prompt_for_features():
    """Interactive mode: prompts user for input"""
    while True:
        try:
            study_hours = float(input("Enter Study Hours: ").strip())
            attendance = float(input("Enter Attendance percentage: ").strip())
            assignments = int(input("Enter number of assignments completed: ").strip())

            return pd.DataFrame([
                {
                    "StudyHours": study_hours,
                    "Attendance": attendance,
                    "Assignments": assignments,
                }
            ])
        except ValueError:
            print("Please enter valid numeric values.")


def get_default_features():
    """Non-interactive mode: returns default test features for CI/CD"""
    return pd.DataFrame([
        {
            "StudyHours": 20.0,
            "Attendance": 85.0,
            "Assignments": 15,
        }
    ])


def main():
    model_path = Path(__file__).parents[1] / "model" / "student_model.pkl"

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found at {model_path}. Please run 'python src/train.py' first."
        )

    model = load(model_path)
    
    # Use non-interactive mode if running in CI/CD (no TTY)
    if not sys.stdin.isatty():
        print("Running in non-interactive mode (CI/CD)")
        sample = get_default_features()
    else:
        print("Running in interactive mode")
        sample = prompt_for_features()

    pred = model.predict(sample)[0]
    print("Prediction:", "Pass" if pred == 1 else "Fail")


if __name__ == "__main__":
    main()
