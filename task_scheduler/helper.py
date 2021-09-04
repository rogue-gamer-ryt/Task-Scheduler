#   Purpose: Helper files to write common functions
from task_scheduler.celery import logger


def helper_method():
    """
    This is a sample script to clean up a folder based on the file extensions

    Returns:
        None
    """
    logger.debug("executing the helper_method")
    return None
