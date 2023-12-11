# Generated by Django 3.2.12 on 2023-09-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230928_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.CharField(blank=True, choices=[('Physik', 'Physik'), ('Kunst', 'Kunst')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='group_institutes',
            field=models.CharField(blank=True, choices=[('IDP', 'IDP'), ('IDM', 'IDM')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='categories',
            field=models.CharField(choices=[('Physik', 'Physik'), ('Kunst', 'Kunst')], default='Physik', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='group_institutes',
            field=models.CharField(choices=[('IDP', 'IDP'), ('IDM', 'IDM')], default='IDP', max_length=10),
        ),
    ]