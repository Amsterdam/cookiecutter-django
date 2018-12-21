#!/bin/bash

# Initialize git repository (Only if it doesn't exist)
function initialize_git {
    if [ ! -e .git ]; then
        git init
        git checkout -b develop
        git remote add origin "{{cookiecutter.git_repository}}"
    fi 
}

function generate_requirements {
    make requirements.txt
}

function docker_up {
    make docker_up
}

function migrate {
    sleep 2
    docker exec {{cookiecutter.project_slug}}_api_1 python ./manage.py migrate
}

initialize_git

echo "Generate Requirements using 'virtualenv'"
generate_requirements
docker_up
migrate

printf -v _hr "%*s" $(expr $(tput lines) - 3) && echo -e ${_hr// /"\n"}
printf -v _hr "%*s" $(tput cols) && echo ${_hr// /=}

echo "Your project has been created in {{cookiecutter.project_slug}}"
