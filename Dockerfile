# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Git to clone the repository
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the repository that contains the src.concrete.ml package
RUN git clone https://github.com/EncryptAI-Protocol/concrete-ml.git --depth=1 /app/src

# Copy the necessary files into the container
COPY requirements.txt /app/requirements.txt
COPY inference.py /app/inference.py

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to run the inference script
ENTRYPOINT ["python", "/app/inference.py"]

# You can also use CMD to specify default arguments that can be overridden
# CMD ["my_model.json", "1234"] 
