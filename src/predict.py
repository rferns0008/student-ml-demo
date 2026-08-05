from joblib import load
from pathlib import Path
import pandas as pd

model = load(Path(__file__).parents[1]/"model"/"student_model.pkl")

sample = pd.DataFrame([{
    "StudyHours":6,
    "Attendance":82,
    "Assignments":7
}])

pred = model.predict(sample)[0]
print("Prediction:", "Pass" if pred==1 else "Fail")
