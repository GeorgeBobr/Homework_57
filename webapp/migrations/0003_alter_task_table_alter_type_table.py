# Generated by Django 5.0 on 2023-12-15 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_type_task_types'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='Task',
        ),
        migrations.AlterModelTable(
            name='type',
            table='Type',
        ),
    ]
