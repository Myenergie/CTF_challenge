# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Add the current directory contents to the Docker image
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run generate_pcap.py when the Docker container launches
CMD ["python", "niveau2.py"]
