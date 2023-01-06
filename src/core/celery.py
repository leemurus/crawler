import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
celery_app = Celery("core")

# Use django config variables with names CELERY_*
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Discover tasks.py in INSTALLED_APPS
celery_app.autodiscover_tasks()
