FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 7860 (standard for Hugging Face Spaces)
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
