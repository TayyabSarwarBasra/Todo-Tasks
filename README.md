# Todo_list_terafort

This is a Django-based web application for managing todo lists and categories.

## Features

- User registration and authentication with token-based authentication.
- CRUD operations for managing todo tasks.
- CRUD operations for managing categories.
- Filter tasks by category.
- Send reminders for upcoming tasks via email.
- Dockerized for easy deployment.

## Installation

1. Clone the repository:
https://github.com/TayyabSarwarBasra/Todo-Tasks.git


2. Install dependencies:

pip install -r requirements.txt



3. Set up the database:
   
   - Configure the PostgreSQL database settings in `settings.py`.
   - Run migrations:
   - python manage.py makemigrations
   - python manage.py migrate
  
## Configuration

Before running the application, make sure to configure the following environment variables:

- `DJANGO_SETTINGS_MODULE`: Set it to `Todo_list_terafort.settings`.
- Database settings: Configure the database connection details.
- Email settings: Configure SMTP settings for sending email reminders.

You can also use a `.env` file to manage environment variables.

## Usage

1. Start the Django server:
2. python manage.py runserver


2. Access the application in your web browser at `http://localhost:8000`.

## Dockerization

To dockerize the application:

1. Build the Docker image:

2. Run the Docker container:









