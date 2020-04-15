# SPC Portal ![Build](https://travis-ci.org/anshulahuja98/spc_portal.svg?branch=master) [![codecov](https://codecov.io/gh/anshulahuja98/spc_portal/branch/master/graph/badge.svg)](https://codecov.io/gh/anshulahuja98/spc_portal) ![Django 2.0.5](https://img.shields.io/badge/Django-2.0.5-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg) 
## A portal for handling Student Placements

### Purpose
 A portal for handling Student Placements


## Building: Quick start with [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers)

This helps you pull and build quickly - dev containers launch the project inside a container with all the tooling required for a consistent and seamless developer experience. 

This means you don't have to install and configure your dev environment as the container handles this for you.

To get started install [VSCode](https://code.visualstudio.com/) and the [Remote Containers extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Clone the repo and launch code:

```bash
git clone https://github.com/anshulahuja98/spc_portal/
cd spc_portal
code .
```

Once VSCode launches run `CTRL+SHIFT+P -> Remote-Containers: Reopen in container` and then use the integrated terminal to run:

- Make database migrations
    ```
    python3 manage.py makemigrations student
    python3 manage.py migrate student
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```

> Note: The first time you run the container it will take some time to build and install the tooling. The image will be cached so this is only required the first time.

## Building: Locally directly

### Installation:
Requirements:   
- Python 3.6 runtime
- Django 2.0.5
- Other dependencies in `requirements.txt`

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     #   spc_portal
    ```
- Create a new virtual environment and activate it.
    ```
    sudo apt-get install -y python3-venv
    python3 -m venv spc_portal_venv
    source spc_portal_venv/bin/activate
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
- Copy .env file
   ```
   cp .env.example .env
   ```
- Make database migrations
    ```
    python3 manage.py makemigrations student
    python3 manage.py migrate student
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```
    
