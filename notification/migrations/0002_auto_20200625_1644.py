# Generated by Django 3.0.7 on 2020-06-25 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='new_notification',
            new_name='notification',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='user_notification',
            new_name='user_notified',
        ),
    ]
