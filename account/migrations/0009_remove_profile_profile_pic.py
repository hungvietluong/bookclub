# Generated by Django 4.2.7 on 2023-11-20 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
