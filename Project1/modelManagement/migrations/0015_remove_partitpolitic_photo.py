# Generated by Django 5.0.2 on 2024-03-28 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelManagement', '0014_partitpolitic_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partitpolitic',
            name='photo',
        ),
    ]