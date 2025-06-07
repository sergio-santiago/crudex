FROM python:3.11-slim
WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "app.py"]
