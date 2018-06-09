# SPC Portal ![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg) ![Django 2.0.5](https://img.shields.io/badge/Django-2.0.5-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

## A portal for handling Student Placements

### Purpose
 A portal for handling Student Placements

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
    python3 -m venv ta_portal_venv
    source spc_portal_venv/bin/activate
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
- Make database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver --settings=ta_portal.settings
    ```
