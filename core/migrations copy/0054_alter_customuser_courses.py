# Generated by Django 4.2.7 on 2023-12-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_rename_institute_movie_institut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='courses',
            field=models.ManyToManyField(default={'Willkommen'}, to='core.course', verbose_name='Kurse'),
        ),
    ]
