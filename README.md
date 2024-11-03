# Django Axes Example Project

This is a simple Django project demonstrating how to implement Django Axes for securing user login by preventing brute-force attempts. The project includes user authentication, login form, and lockout functionality when a user exceeds the allowed number of failed login attempts.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Testing](#testing)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.6 or higher)
- pip (Python package installer)
- Django (3.2 or higher)

## Installation

1. **Clone the repository:**

   Open your terminal and run the following command:

   ```bash
   git clone https://github.com/dhanvina/django-axes.git
   cd django-axes
2. **Install the required packages:**

    Install Django and Django Axes using pip:

    ```bash
    pip install django django-axes
3. **Apply migrations:**

    Run the following command to set up the database and apply migrations, including those for Django Axes:

    ```bash
    python manage.py migrate
4. **Create a superuser account:**

    You need a superuser to access the Django admin interface and manage users

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username and password.

## Running the Project

1. **Start the development server:**

    Run the following command to start the server:

    ```bash
    python manage.py runserver
2. **Access the application:**

    Open your web browser and go to **http://127.0.0.1:8000/login/** to access the login page.

3. **Log in:**

    Use the superuser credentials you created earlier to log in. You can also attempt to log in with incorrect credentials to test the lockout feature

## Testing

1. **Attempt Failed Logins:**

    Go to the login page and try logging in with incorrect credentials three times. After the third failed attempt, you will be redirected to a lockout page.

2. **View Axes Attempts in Admin:**

    Go to the Django admin interface at http://127.0.0.1:8000/admin/ and log in with your superuser credentials. You will see a section for Axes attempts where you can manage failed login attempts.