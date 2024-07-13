# Generated by Django 4.2.13 on 2024-06-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanager', '0005_remove_jobpost_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='requirements',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.ManyToManyField(to='jobmanager.skills'),
        ),
    ]
