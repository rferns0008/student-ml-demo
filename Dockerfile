FROM python3.13-slim

WORkdir /app

copy . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COMMAND ["python", "predict.py"]