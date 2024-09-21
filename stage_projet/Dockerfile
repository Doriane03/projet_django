# Use the official Python image from the DockerHub
FROM python:3.12.3-slim

ENV PYTHONDONTWRITEBYTE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]