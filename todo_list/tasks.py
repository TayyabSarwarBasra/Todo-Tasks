from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from .models import Todo
from django.utils import timezone


@shared_task(blind=True)
def send_reminders():
    todos = Todo.objects.filter(deadline__lte=timezone.now() + timedelta(days=1),
                                status__in=['todo', 'qa', 'in_progress'])
    for todo in todos:
        send_mail(
            f"Reminder: {todo.title}",
            f"Don't forget to complete {todo.title} before {todo.deadline}.",
            'tayyabbasra434@gmail.com',
            [todo.user.email],
            fail_silently=False,
        )

