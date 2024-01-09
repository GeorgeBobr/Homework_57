# Generated by Django 5.0 on 2024-01-08 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_project_task_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]