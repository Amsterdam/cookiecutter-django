FROM amsterdam/python
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir -p /static && chown datapunt /static

COPY src /app/
COPY deploy /deploy/
COPY requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

USER datapunt

RUN export SECRET_KEY=insecure
RUN export DJANGO_SETTINGS_MODULE={{ cookiecutter.project_slug }}.settings.development

RUN python manage.py collectstatic --no-input

CMD uwsgi