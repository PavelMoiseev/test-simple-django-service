# pull official base image
FROM python:3.10.4

# set work directory
RUN mkdir /hello_rekruto
WORKDIR /hello_rekruto

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /hello_rekruto/
RUN pip install -r requirements.txt

# copy project
COPY . /hello_rekruto/

