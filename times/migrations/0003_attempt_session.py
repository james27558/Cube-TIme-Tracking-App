# Generated by Django 4.0 on 2022-01-17 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0002_attempt_remove_session_session_id_session_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='times.session'),
            preserve_default=False,
        ),
    ]
