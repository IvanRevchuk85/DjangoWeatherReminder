import os
from celery import Celery


#  Specifying default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "django_weather_reminder.settings")

# Creating an application Celery
app = Celery("django_weather_reminder")

# Preparing Celery to read settings from Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically search for tasks in tasks.py file in all installed applications
app.autodiscover_tasks()
