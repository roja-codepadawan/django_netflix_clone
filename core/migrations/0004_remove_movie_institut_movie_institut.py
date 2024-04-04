# Generated by Django 4.2.7 on 2024-04-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_institute_alter_customuser_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='institut',
        ),
        migrations.AddField(
            model_name='movie',
            name='institut',
            field=models.ManyToManyField(to='core.institute', verbose_name='Institute'),
        ),
    ]
