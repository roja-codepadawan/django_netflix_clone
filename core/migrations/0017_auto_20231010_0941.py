# Generated by Django 3.2.12 on 2023-10-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_customuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cours',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='institut',
            field=models.CharField(blank=True, choices=[('IDP', 'IDP'), ('IDM', 'IDM')], max_length=20, null=True),
        ),
    ]
