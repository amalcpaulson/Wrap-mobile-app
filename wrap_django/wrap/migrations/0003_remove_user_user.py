# Generated by Django 4.0.4 on 2023-03-24 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0002_user_photo_user_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]