# syntax=docker/dockerfile:1

# Base Image (preconfigured OS - :3 indicates specific build of Base Image Python)
FROM python:3 

# The work directory app. (has copy of content and docker works in here)
WORKDIR /weathermania-docker

# Copy the requirements.txt into the container image's requirement.txt file.
COPY requirements.txt requirements.txt

# Install all dependencies from .txt file
RUN pip3 install -r requirements.txt

# Copy remainder of files into image directory
COPY . . 

# ------ Now we help docker understand how to run image inside a container ------

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]