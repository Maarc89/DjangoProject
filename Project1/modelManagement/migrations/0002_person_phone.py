# Generated by Django 5.0.3 on 2024-03-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
