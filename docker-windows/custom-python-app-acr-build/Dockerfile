#
#In this Docker file are pulling an image from ACR with Python already installed
#
ARG BASE_REGISTRY
FROM ${BASE_REGISTRY}/python3.9-baseimage:latest


# Set the working directory in the container
WORKDIR /app
# Copy requirements file
COPY requirements.txt .
COPY pytest.ini .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the source code
COPY src/ ./src/
COPY tests/ ./tests/


# Run pytest during build
ENV PYTHONPATH=/app/src;/app;/app/tests
RUN python -m pytest tests/ -v --tb=short

# Set the working directory to src for execution
WORKDIR /app/src
# Command to run the application
CMD ["python", "demo.py"]