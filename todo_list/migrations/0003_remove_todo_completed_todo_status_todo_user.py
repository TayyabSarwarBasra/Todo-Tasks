# Generated by Django 4.2.11 on 2024-04-09 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_list', '0002_alter_todo_category_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In Progress'), ('qa', 'QA'), ('done', 'Done')], default='todo', max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
