# Generated by Django 3.2.12 on 2023-09-28 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230927_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video_id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_title',
        ),
    ]
