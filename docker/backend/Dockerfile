FROM ubuntu:22.04
# Create working directory
#c'est le dossier ou docker va stocker mes informations
WORKDIR /home/app  
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#USER app
# Update package repository and install required packages
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y python3 python3-pip supervisor postgresql-client postgresql-server-dev-all gcc g++ \
    curl netcat nano libldap2-dev libsasl2-dev libssl-dev

# Upgrade pip and install gunicorn
RUN pip3 install --upgrade pip && pip3 install gunicorn
RUN apt-get update && apt-get install -y redis-tools
# Copy requirements and install them
COPY ./requirements.txt /home/app/
RUN pip3 install -r requirements.txt

# Copy your application files
COPY ./stage_projet /home/app/backend  
#j'ai modifié le premier COPY en ajoutant stage_projet
COPY ./docker /home/app/docker

# Copy Supervisor configuration files
COPY ./docker/supervisor/supervisord.conf /etc/supervisor/conf.d/
#new
COPY ./docker/supervisor/celery.conf /etc/supervisor/conf.d/celery.conf 


# Make entrypoint scripts executable
RUN chmod +x /home/app/docker/backend/server-entrypoint.sh
RUN chmod +x /home/app/docker/backend/daemon-entrypoint.sh

CMD ["celery", "-A", "stage_projet", "worker", "--loglevel=info"]