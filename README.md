# Productivity API

A task management REST API built with Django and Django REST Framework.

## Features

- User authentication
- Create tasks
- Update tasks
- Delete tasks
- View tasks

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

GET /tasks  
POST /tasks  
PUT /tasks/{id}  
DELETE /tasks/{id}

## How to Run Locally

1. Clone the repository

git clone https://github.com/Iamojochenemi/productivity-api.git

2. Navigate into the folder

cd productivity-api

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start the server

python manage.py runserver
