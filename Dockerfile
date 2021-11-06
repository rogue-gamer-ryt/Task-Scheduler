FROM python:3.6-alpine

# Install dependencies required for psycopg2 python package
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN mkdir -p /task_scheduler
WORKDIR /task_scheduler
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# Remove dependencies only required for psycopg2 build
RUN apk --purge del .build-deps

EXPOSE 8000
