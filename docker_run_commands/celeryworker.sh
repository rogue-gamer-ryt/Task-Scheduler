#!/bin/sh
wget -qO- https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for | sh -s -- postgres:5432 -- echo success &
wget -qO- https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for | sh -s -- task_scheduler:8000 -- echo success &
celery -A task_scheduler worker -l info
