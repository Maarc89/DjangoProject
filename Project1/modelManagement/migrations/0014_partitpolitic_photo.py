# Generated by Django 5.0.2 on 2024-03-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelManagement', '0013_remove_reunio_politic'),
    ]

    operations = [
        migrations.AddField(
            model_name='partitpolitic',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='partit_photos/'),
        ),
    ]