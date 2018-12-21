# {{ cookiecutter.project_slug }} #


### Install procedure ###

```
git clone {{ cookiecutter.git_repository }} {{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
```

Start the docker containers manually
```
docker-compose up -d
```

#### Local development ####

To create the virtualenvironment (python3) and install requirements run:
```
make virtualenv
```

{{ cookiecutter.project_slug }} API
==================

This is a standard Django Rest Framework API.

```
docker-compose up database
python manage.py runserver
```
