# pull official base image
FROM python:3.9.5-alpine

# set work directory
WORKDIR /usr/src/parser

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
#RUN pip freeze > requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
