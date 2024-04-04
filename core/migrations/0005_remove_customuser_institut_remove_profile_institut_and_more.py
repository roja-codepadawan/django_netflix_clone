# Generated by Django 4.2.7 on 2024-04-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_movie_institut_movie_institut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='institut',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='institut',
        ),
        migrations.AddField(
            model_name='customuser',
            name='institut',
            field=models.ManyToManyField(to='core.institute', verbose_name='Institute'),
        ),
        migrations.AddField(
            model_name='profile',
            name='institut',
            field=models.ManyToManyField(to='core.institute', verbose_name='Institute'),
        ),
    ]
