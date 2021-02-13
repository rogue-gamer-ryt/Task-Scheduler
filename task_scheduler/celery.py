#   Purpose: Celery initialization and django integration file


import os

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings

from task_scheduler.helper import shift_files

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
def organize_files(path: str):
    """
    Task to check the disk usage and send an alert if the threshold has been breached
    Args:
        path (str): path of the folder

    Returns:

    """
    try:
        shift_files(path)
    except Exception:
        logger.error("Exception occurred")
