# Generated by Django 3.2.12 on 2023-10-26 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_rename_cours_customuser_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Kurse'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile'},
        ),
    ]
