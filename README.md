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

## Authentication Example

### JWT Authentication

POST /api/token/  
Body:
{
  "username": "amos",
  "password": "yourpassword"
}

Response:
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

## Pagination Example

GET /todos/?page=1  
Headers:
Authorization: Bearer <access_token>

Response:
{
  "count": 25,
  "next": "/todos/?page=2",
  "previous": null,
  "results": [
    { "id": 1, "title": "Buy milk", "completed": false, ... },
    { "id": 2, "title": "Finish project", "completed": true, ... }
  ]
}


## Filtering Example

GET /todos/?status=completed  
Headers:
Authorization: Bearer <access_token>

Response:
[
  { "id": 2, "title": "Finish project", "completed": true, ... },
  { "id": 5, "title": "Call client", "completed": true, ... }
]


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
