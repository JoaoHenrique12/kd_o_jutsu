FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 5000

CMD ["uvicorn", "src.production:asgi_app", "--host", "0.0.0.0", "--port", "5000"]
