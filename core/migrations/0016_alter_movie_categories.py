# Generated by Django 3.2.12 on 2023-08-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_movie_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=models.CharField(choices=[('Physik', 'Physik'), ('Kunst', 'Kunst')], max_length=10),
        ),
    ]
