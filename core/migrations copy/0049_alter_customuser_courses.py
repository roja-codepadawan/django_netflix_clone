# Generated by Django 3.2.12 on 2023-10-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_alter_customuser_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='courses',
            field=models.ManyToManyField(default='Willkommen', to='core.Course', verbose_name='Kurse'),
        ),
    ]
