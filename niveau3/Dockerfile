# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY network_traffic.pcap /app/
COPY level3_challenge.py /app/

# Install the required dependencies
RUN pip install scapy

# Set the command to be executed when the container starts
CMD [ "python", "level3_challenge.py" ]
