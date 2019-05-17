# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /amoo_jozve_foroosh

# Set the working directory to /amo_jozve_forosh
WORKDIR /amoo_jozve_foroosh

# Copy the current directory contents into the container at /amoo_jozve_foroosh
ADD . /amoo_jozve_foroosh/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements/development.txt
