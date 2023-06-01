# Dockerfile

# Use lightweight Python image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the Python script and input image into the container
COPY cipher_steg.py input_image.png ./

# Install necessary Python package
RUN pip install --no-cache-dir stegano

# Run the Python script when the container starts
CMD ["python", "niveau1.py"]