# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages, including git and Python 3.10.6
RUN apt-get update && \
    apt-get install -y git python3.10 python3.10-venv python3-pip cmake protobuf-compiler && \
    apt-get clean

# Ensure pip is linked to Python 3.10 version and create necessary symbolic links
RUN ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Upgrade pip, wheel, and setuptools
RUN pip install --upgrade pip wheel setuptools

# Install concrete-ml
RUN pip install concrete-ml

# Set the working directory
WORKDIR /app

# Clone the repository containing the necessary files
RUN git clone https://github.com/EncryptAI-Protocol/concrete-ml.git

# Add the src directory to the Python path
ENV PYTHONPATH="${PYTHONPATH}:/app/concrete-ml/src"

# Set the entrypoint to run inference.py
ENTRYPOINT ["python", "/app/concrete-ml/inference.py"]
