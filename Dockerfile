# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Git to clone the repository
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the repository that contains the src.concrete.ml package
RUN git clone https://github.com/EncryptAI-Protocol/concrete-ml.git --depth=1 /app/src

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Install the Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the inference script
COPY inference.py /app/inference.py

# Set the entry point to run the inference script
ENTRYPOINT ["python", "/app/inference.py"]
