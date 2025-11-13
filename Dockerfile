# Use the official Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY requirements.txt .
COPY app.py .
COPY client.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask server
CMD ["python", "app.py"]
