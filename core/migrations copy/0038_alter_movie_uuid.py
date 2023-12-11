# Generated by Django 3.2.12 on 2023-10-30 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_movie_age_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=None, unique=True),
        ),
    ]