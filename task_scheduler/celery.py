#   Purpose: Celery initialization and django integration file

import os

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings

from task_scheduler.helper import helper_method

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_scheduler.settings')
app = Celery('task_scheduler')
# Celery will apply all configuration keys with defined namespace
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load tasks from all registered apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# Setup worker logger
logger = get_task_logger(__name__)


@app.task
def task_one():
    """
    High-level task details


    Returns:
        None
    """
    try:
        logger.info("Launching task_one")
        helper_method()
    except Exception:
        logger.error("Exception occurred")
