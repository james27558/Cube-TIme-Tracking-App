# Generated by Django 4.0 on 2022-01-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0004_attempt_datetime_attempt_note_alter_attempt_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='date',
        ),
        migrations.AddField(
            model_name='session',
            name='endDateTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='startDateTime',
            field=models.DateTimeField(null=True),
        ),
    ]
