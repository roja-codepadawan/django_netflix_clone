# Generated by Django 3.2.12 on 2023-10-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20231023_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('Studierende', 'Studierende'), ('Mitarbeiter', 'Mitarbeiter')], max_length=20, null=True),
        ),
    ]
