# Generated by Django 3.2.6 on 2022-09-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220913_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='img/faces/avatar.jpg', null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture'),
        ),
    ]
