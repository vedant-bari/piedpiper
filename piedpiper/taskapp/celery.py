import os
import django
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings
from celery.decorators import task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piedpiper.config")

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

#import configurations
#configurations.setup()

from configurations import importer
importer.install()


app= Celery('piedpiper.taskapp',broker='amqp://admin:mypassword@rabbit:5673', backend='redis://redis:6379/0')

app.conf.update(
        CELERY_TASK_SERIALIZER = 'json',
        CELERY_RESULT_SERIALIZER = 'json',
                )


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@task(name="sum_two_numbers")
def add(x, y):
    return x + y
