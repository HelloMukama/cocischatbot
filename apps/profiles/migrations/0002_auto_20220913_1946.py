# Generated by Django 3.2.6 on 2022-09-13 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='activated',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email_verified',
        ),
    ]
