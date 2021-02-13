#
#   Purpose: WSGI configuration file
#     WSGI config for server project.
#
#     For more information on this file, see
#     https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_scheduler.settings")

application = get_wsgi_application()
