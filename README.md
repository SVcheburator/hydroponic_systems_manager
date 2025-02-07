# Hydroponic System API

This is a Django REST Framework project for managing hydroponic systems and their measurements.

## Features
- User authentication & registration
- CRUD operations for hydroponic systems
- CRUD operations for measurements
- API documentation with Swagger & ReDoc

## Installation steps
1) Clone the repository 

https:
``` 
git clone https://github.com/SVcheburator/hydroponic_systems_manager.git
```
ssh:
```
git clone git@github.com:SVcheburator/hydroponic_systems_manager.git
```
```
cd hydroponic_systems_manager
```
2) Create a virtual environment
```
python -m venv venv
```
```
venv\Scripts\activate
```
3) Install dependencies
```
pip install -r requirements.txt
```
4) Create your psql database
5) go to project directory
```
cd hydroponic_system
```

6) Create and fill your .env file
```
SECRET_KEY=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=
POSTGRES_HOST= 
```
7) Migrate the database
```
python manage.py migrate
```
8) Create a superuser
```
python manage.py createsuperuser
```
9) Run the server
```
python manage.py runserver
```

## Start using
Go to http://127.0.0.1:8000/ and start using the app.

## API Documentation
- Swagger: http://127.0.0.1:8000/swagger/
- ReDoc: http://127.0.0.1:8000/redoc/