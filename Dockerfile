FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Set environment variables for Gunicorn
ENV PYTHONUNBUFFERED=1
ENV GUNICORN_WORKERS=1
ENV GUNICORN_THREADS=1
ENV GUNICORN_TIMEOUT=120

CMD ["gunicorn", "--workers", "1", "--threads", "1", "--timeout", "120", "--bind",  "0.0.0.0:8000","api:create_app()"]


