import os
from datetime import timedelta

from django.conf import settings

from celery import Celery
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

# Initialize Celery
app = Celery("core")

# Auto-discover tasks from installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery Configuration
app.conf.broker_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_URL_BROKER}"
app.conf.result_backend = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_URL_BROKER}"

# Serialization settings
app.conf.task_serializer = "json"
app.conf.result_serializer = "json"
app.conf.accept_content = ["json"]

# Task result expiration and prefetch multiplier
app.conf.task_always_eager = False
app.conf.worker_prefetch_multiplier = 4
app.conf.result_expires = timedelta(days=1)

# Beat schedule configuration
app.conf.beat_schedule = {

}

# Connection Retry on Startup
app.conf.broker_connection_retry_on_startup = True
