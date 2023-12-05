# Generated by Django 3.2.12 on 2023-10-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20231026_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='course',
        ),
        migrations.AddField(
            model_name='customuser',
            name='course',
            field=models.ManyToManyField(to='core.Course'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group_course',
        ),
        migrations.AddField(
            model_name='profile',
            name='group_course',
            field=models.ManyToManyField(to='core.Course'),
        ),
    ]