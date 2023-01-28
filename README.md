# Django REST API

This is a Django REST API project that allows users to interact with a database via HTTP requests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x
- pip

### Installing

1. Clone the repository
> git clone https://github.com/olsihoxha/timetracker.git



2. Change into the project directory
> cd timetracker



3. Install the required packages
> pip install -r requirements.txt



4. Apply migrations

***You need to set up the database first and then change it in the settings.py***
> python manage.py makemigrations

> python manage.py migrate



5. Run the server

> python manage.py runserver


*By default the server will be running on `http://127.0.0.1:8000/`*


