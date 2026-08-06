# Student ML Demo

![CI](https://github.com/rferns0008/student-ml-demo/actions/workflows/ci.yml/badge.svg)

A simple ML project (without CI/CD) for training and serving predictions locally.

Run:

```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
```

When you run the prediction script, it will prompt you for:
- Study Hours
- Attendance percentage
- Number of assignments completed
