
#   Purpose: Define the Project level URLs over here

from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'', admin.site.urls),
]
admin.site.site_header = "Task Scheduler Admin"
admin.site.site_title = "Task Scheduler Admin Portal"
admin.site.index_title = "Configure your tasks"
