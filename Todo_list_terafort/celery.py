from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_list_terafort.settings')

app = Celery('Todo_list_terafort')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'send-reminders-every-day': {
        'task': 'todo_list.tasks.send_reminders',
        'schedule': crontab(minute='17', hour='17')
    },
}
app.conf.timezone = 'Asia/Karachi'



