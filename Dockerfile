# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /action

# Copy the Python script and dependencies to the container
COPY check_hardcoded_ip.py /action/check_hardcoded_ip.py

# Install any dependencies if necessary (none in this case)
# RUN pip install <your-dependency>

# The command to run when the container starts
CMD ["python", "/action/check_hardcoded_ip.py"]
