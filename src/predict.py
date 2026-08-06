from joblib import load
from pathlib import Path
import pandas as pd


def prompt_for_features():
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


def main():
    model_path = Path(__file__).parents[1] / "model" / "student_model.pkl"

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found at {model_path}. Please run 'python src/train.py' first."
        )

    model = load(model_path)
    sample = prompt_for_features()

    pred = model.predict(sample)[0]
    print("Prediction:", "Pass" if pred == 1 else "Fail")


if __name__ == "__main__":
    main()
