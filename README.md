# Datapunt Django template

This project contains the base template for django projects.


## Usage

### Requirements
- You need `make`, `python3` and `virtualenv` in order to use this project

### Creating a project

To create a project, you just have to run `make project` and follow the prompts.

Your project will be created in a directory that you can (and should) move to your development directory.

The project will have git initialized in a `master` branch and with the `origin` set to the git repository you specified in the prompts.

## Project Contents

The template will contain the following:

- Dockerized environments for the services needed to run the project (eg. postgres) `docker-compose.yml`
- Automated tests using `tox` `pytest` and `factory-boy`
