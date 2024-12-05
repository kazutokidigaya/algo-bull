# To-Do List App

## Overview

This project is a To-Do List backend application built with Django and Django REST Framework (DRF). It allows users to manage tasks, including setting timestamps, adding titles, descriptions, due dates, tags, and statuses.

The app is deployed on Railway, and the backend can be accessed via REST APIs. The project includes unit, integration, and end-to-end tests, along with GitHub Actions for continuous integration and deployment.

## Project Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/kazutokidigaya/algo-bull.git
cd algobulls
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

3. Set Environment Variables

```bash
export DATABASE_URL="postgresql://<your-username>:<your-password>@<your-db-host>:5432/your-db-name"
export SECRET_KEY="your-generated-secret-key"
export DEBUG=True
```

To create Database URL (DATABASE_URL) Using Railway:

1.Go to Railway.
2.Create a free account or log in if you already have one.
3.Create a new project.
4.Add a PostgreSQL plugin to your project.
5.Copy the DATABASE_URL from the Environment Variables section of your Railway dashboard.

4. Run Migrations

```bash
python manage.py migrate
```

5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password.

6. Run the Development Server

```bash
python manage.py runserver
```

## API Endpoints

The following are the available endpoints for the To-Do List App also before running them head to authorization tab in your postman and slecet Basic Auth give the name and password and then run the below endpoint:

1. Create a Task
   URL: /api/tasks/
   Method: POST
   Body:

```bash
{
  "title": "Test Task",
  "description": "This is a test task.",
  "due_date": "2024-12-05",
  "tags": "work,priority",
  "status": "OPEN"
}
```

2. Retrieve All Tasks
   URL: /api/tasks/
   Method: GET
   Response: A list of tasks in JSON format.

3. Retrieve a Task by ID
   URL: /api/tasks/{id}/
   Method: GET
   Response: A single task object with the specified id.

4. Update a Task
   URL: /api/tasks/{id}/
   Method: PUT
   Body:

```bash
{
  "title": "Updated Task",
  "description": "Updated description",
  "due_date": "2024-12-10",
  "tags": "work,high-priority",
  "status": "WORKING"
}
```

5. Delete a Task
   URL: /api/tasks/{id}/
   Method: DELETE
   Response: 204 No Content

## Tests

To run the tests:

```bash
python manage.py test
```

## Deployment

The app is deployed on Railway at:

https://web-production-a140f.up.railway.app/
