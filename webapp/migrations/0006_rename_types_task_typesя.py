# Generated by Django 5.0 on 2023-12-15 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_type_task_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='types',
            new_name='typesя',
        ),
    ]
