# Generated by Django 3.1.7 on 2021-07-05 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='Follower',
            new_name='follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='Following',
            new_name='following',
        ),
    ]
