# Generated by Django 3.1.3 on 2022-11-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_remove_submission_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='choices',
            field=models.ManyToManyField(to='onlinecourse.Choice'),
        ),
    ]
