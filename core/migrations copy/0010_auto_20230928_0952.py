# Generated by Django 3.2.12 on 2023-09-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230928_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='group_institutes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group_institutes',
        ),
    ]