# Generated by Django 3.2.12 on 2023-10-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20231023_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cours',
            field=models.CharField(blank=True, choices=[('Willkommen', 'Willkommen'), ('1', '1'), ('2', '2')], default='Willkommen', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='institut',
            field=models.CharField(blank=True, choices=[('Willkommen', 'Willkommen'), ('IDP', 'IDP'), ('IDM', 'IDM')], default='Willkommen', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='group_courses',
            field=models.CharField(blank=True, choices=[('Willkommen', 'Willkommen'), ('1', '1'), ('2', '2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='group_institutes',
            field=models.CharField(blank=True, choices=[('Willkommen', 'Willkommen'), ('IDP', 'IDP'), ('IDM', 'IDM')], max_length=20, null=True),
        ),
    ]