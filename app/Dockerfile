FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (good practice for Docker caching)
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY ./app /app

# Expose the port the container will listen on (using default as placeholder)
EXPOSE 8000

# Command to run the application using the PORT environment variable
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]
