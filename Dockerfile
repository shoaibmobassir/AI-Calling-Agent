# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add environment (in production use secrets manager)
ENV PYTHONUNBUFFERED=1

# Start point (you can override in docker-compose)
CMD ["python", "main.py"]
