# Generated by Django 4.2.13 on 2024-06-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanager', '0009_alter_jobpost_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]
