# Inherit the base image
FROM python:3.8.0
ENV PYTHONUNBUFFERED=1

# Create working directory
RUN mkdir /code
WORKDIR /code

# Add required files
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt 
COPY . /code/

# Set SQLite
RUN python manage.py migrate

# Install modules
RUN apt-get update && apt-get install expect -y

# Set Admin. user for app & SQLite
RUN expect createsuperuser.exp

# Expose 8000 port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]