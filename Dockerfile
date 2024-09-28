FROM python:3.10.6-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if needed) and Git for cloning repositories
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Upgrade pip, install wheel, setuptools, and concrete-ml
RUN pip install --upgrade pip wheel setuptools && \
    pip install concrete-ml

# Copy your local repository files into the container
COPY ./ /app/src

# Set the PYTHONPATH environment variable to include your src directory
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Copy the inference script
COPY inference.py /app/inference.py

# Copy the necessary CSV files into the container (e.g., x_train.csv)
COPY x_train.csv /app/x_train.csv

# Set the entry point to run the inference script with argumentss
ENTRYPOINT ["python", "/app/inference.py"]