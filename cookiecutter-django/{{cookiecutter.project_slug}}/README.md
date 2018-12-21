# {{ cookiecutter.project_slug }} #


### Install procedure ###

```
git clone https://github.com/Amsterdam/afvalcontainers.git {{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
```

Start the docker database and run the download en upload scripts.
```
docker-compose build
docker-compose up
```

#### Local development ####

Create a local environment and activate it:
```
virtualenv --python=$(which python3) venv
source venv/bin/activate
```

Start development database


```
	docker-compose up database
```


```
pip install -r requirements.txt
```


{{ cookiecutter.project_slug }} API
==================

This is a standard Django Rest Framework API.

```
	docker-compose up database
	python manage.py runserver
```


