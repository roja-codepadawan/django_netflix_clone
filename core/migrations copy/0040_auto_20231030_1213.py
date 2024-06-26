# Generated by Django 3.2.12 on 2023-10-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20231030_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('single', 'Single'), ('seasonal', 'Seasonal')], help_text='Einzel Film oder Serie(Veranstaltungsreihe)', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='group_institut',
            field=models.CharField(choices=[('Willkommen', 'Willkommen'), ('IDP', 'IDP'), ('IDM', 'IDM')], max_length=20, null=True, verbose_name='Institut'),
        ),
    ]
