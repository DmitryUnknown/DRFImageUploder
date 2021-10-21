FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN apt-get update && apt-get install -y && /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN pip install -r requirements.txt

#EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
#CMD python manage.py makemigrations && python manage.py migrate
