# Generated by Django 3.0.7 on 2020-06-25 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_remove_notification_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='which_tweet',
            new_name='tweet',
        ),
    ]
