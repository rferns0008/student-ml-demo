import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
from pathlib import Path

df = pd.read_csv(Path(__file__).parents[1]/"data"/"student_data.csv")
X = df[["StudyHours","Attendance","Assignments"]]
y = df["Pass"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X,y)

out = Path(__file__).parents[1]/"model"/"student_model.pkl"
dump(model,out)
print(f"Model saved to {out}")
