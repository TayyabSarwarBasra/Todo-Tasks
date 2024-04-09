from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):

    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In Progress'),
        ('qa', 'QA'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=LOW)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


