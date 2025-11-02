FROM python:3.11-slim

WORKDIR /app

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копіювання requirements файлів
COPY requirements.txt .

# Встановлення Python залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання коду застосунку
COPY app/ ./app/

# Створення non-root користувача
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Експонування порту
EXPOSE 8000

# Команда запуску
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]