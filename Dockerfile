FROM python:3.5.2

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD python manage.py db upgrade && python manage.py runserver -h 0.0.0.0
