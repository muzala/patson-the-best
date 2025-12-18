FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies (if needed, uncomment below lines for requirements.txt)
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "my.py"]