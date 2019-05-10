# SPC Portal ![Build](https://travis-ci.org/anshulahuja98/spc_portal.svg?branch=master)  ![Django 2.0.5](https://img.shields.io/badge/Django-2.0.5-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

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
>In case of any issues in running migrations, comment out this [line](https://github.com/anshulahuja98/spc_portal/blob/03a89e9982487fef71f422d400d4e39daf5b5f2f/src/accounts/forms.py#L33) and the do the above steps then uncomment it and repeat.    

- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```
    
