
FROM python:3.10-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


    

# set work directory
WORKDIR /app
# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install gunicorn
RUN pip install Pillow



 


# copy project
COPY . .
RUN pip install -r requirements.txt



EXPOSE 8080



CMD gunicorn dict.wsgi:application --bind 0.0.0.0:$PORT