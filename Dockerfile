From python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /backend_mjes
WORKDIR /backend_mjes
COPY requirements.txt /backend_mjes/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /backend_mjes/
RUN python manage.py makemigrations
