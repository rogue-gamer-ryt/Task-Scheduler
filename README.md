# Task Scheduler
## Overview
This project is to create a service that could run and manage a task/script at a specific time.

## Setup
To run this project you can use docker to quickly do the setup for redis, postgres and workers

### Using `docker`
#### 1. Create a .env file at the root directory and add the following text to it
```env
DEBUG=True
DJANGO_LOG_LEVEL=DEBUG
DJANGO_SECRET_KEY=<PUT YOUR SECRET KEY>
DJANGO_SUPERUSER_EMAIL="admin@xyz.com"
DJANGO_SUPERUSER_PASSWORD="admin"
DJANGO_SUPERUSER_USERNAME="admin"
```
#### 2. Use this command to bring everything up.    
```sh
docker-compose up
```

#### 3. This will create 4 containers, more details below
- **task_scheduler**: This the web app where you can manage the tasks like add, remove, schedule and etc.
- **postgres**: Postgres is being used as the DB for this project. It will be running on its default port ```5432```
- **celery_worker**: This instance will run the scheduled tasks. You can modify the number of workers inside this instance.
- **celery_beat**: Celery beat is responsible for assigning tasks to the celery workers whenever they are scheduled
- **redis**: We are using redis as a message broker

_To know more about it, check out the ```docker-compose.yaml``` of the project_

### Using `runserver`
####  1. You can update the database configuration in `settings.py`. For this method we will use the database configuration for sqlite
```
Line: 121
# THIS WILL CONNECT TO SQLITE DATABASE. USE THIS IF YOU WANT TO RUN IT DIRECTLY USING
# COMMAND 'python manage.py runserver
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'task_database',  # This is where you put the name of the db file.
#         # If one doesn't exist, it will be created at migration time.
#     }
# }

# USE THIS DATABASE CONFIGURATION IF YOUR ARE RUNNING IT WITH DOCKER
# THIS WILL CONNECT TO POSTGRES CONTAINER WHEN 'docker-compose up' is used

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'task_scheduler',
        "USER": 'admin',
        "PASSWORD": 'dbpassword',
        "HOST": 'postgres',
        "PORT": '5432',
        "TEST": {"NAME": "test_task_scheduler"},
    }
}
```
#### 2. Start `redis` server or update `redis` server configuration
**Start redis server**
- To start redis-server you can start via docker - `docker-compose up redis`
- Or, download from [here](https://download.redis.io/releases/redis-6.2.6.tar.gz)

**Update server configuration**
- You can update the redis host in your `settings.py`
```
Line : 103
# Settings for celery and redis configurations
redis_host = 'redis'
CELERY_BROKER_URL = f'redis://{redis_host}:6379'
```
#### 3. You could also run the application by using the command
```sh
python3 manage.py runserver
```
For this either update the postgres connection settings based on your database in the ```settings.py``` file or you could use SQLite connection details inside the same file.

#### 4. The application should be up and now we need to start our celery worker and celery beat.  

Command to start celery worker:
```
celery -A task_scheduler worker -l info
```
Command to start celery beat: 
```
celery -A task_scheduler beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
## Additional link
- You can read more about this project over [here](https://ashun.vercel.app/blog/task-scheduler)

## Tech Stack reference

* [Django](https://www.djangoproject.com/start/) - Getting started with Django
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html) - Getting started with Celery
* [Redis](https://redis.io/) - Our message broker
* [Postgres](https://www.postgresql.org/) - "The World's Most Advanced Open Source Relational Database"
