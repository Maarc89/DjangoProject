# Generated by Django 5.0.3 on 2024-03-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelManagement', '0003_partitpolitic_politic_reunio_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politic',
            name='phone',
        ),
        migrations.AddField(
            model_name='politic',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='politic',
            name='partit',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='politic',
            name='carrec',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
