import os
from celery import Celery


#  Указываем настройки Django по умолчанию
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_weather_reminder.settings")

# Cоздаем приложения Celery
app = Celery("django_weather_reminder")

# Готовим Celery читать настройки из Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически искать таски в файлвх tasks.py во всех установленных приложениях
app.autodiscover_tasks()
