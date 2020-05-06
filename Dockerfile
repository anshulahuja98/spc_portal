FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE spc_django.settings

RUN mkdir /dist
WORKDIR /dist

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
WORKDIR /dist/src
RUN ls
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT ["/dist/entrypoint.sh"]
