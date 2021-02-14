# Task Scheduler
## Overview
This project is to create a service that could run and manage a task at a specific time.

## Setup
To run this project you can use docker to quickly do the setup for redis, postgres and workers

### Using Docker
Use this command to bring everything up.    
```sh
$ docker-compose up
```

This will create 4 containers, more details below
- **task_scheduler**: This the web app where you can manage the tasks like add, remove, schedule and etc.
- **postgres**: Postgres is being used as the DB for this project. It will be running on its default port ```5432```
- **celery_worker**: This instance will run the scheduled tasks. You can modify the number of workers inside this instance.
- **celery_beat**: Celery beat is responsible for assigning tasks to the celery workers whenever they are scheduled
- **redis**: We are using redis as a message broker

To know more about it, check out the ```docker-compose.yaml``` of the project

### Using runserver
You could also run the application by using the command
```sh
$ python3 manage.py runserver
```
For this either update the postgres connection settings based on your database in the ```manage.py``` file or you could use SQLite connection details inside the same file.

## Tech Stack reference

* [Django](https://www.djangoproject.com/start/) - Getting started with Django
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html) - Getting started with Celery
* [Redis](https://redis.io/) - Our message broker
* [Postgres](https://www.postgresql.org/) - "The World's Most Advanced Open Source Relational Database"
