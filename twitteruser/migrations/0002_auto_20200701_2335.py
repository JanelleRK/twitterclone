# Generated by Django 3.0.8 on 2020-07-01 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twitteruser',
            old_name='following',
            new_name='followers',
        ),
    ]