# Generated by Django 3.2.12 on 2023-09-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230928_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('file', models.FileField(upload_to='movies')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_file',
        ),
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Kids', 'Kids'), ('Studi', 'Studi'), ('Prof', 'Prof')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids'), ('Studi', 'Studi'), ('Prof', 'Prof')], max_length=5),
        ),
        migrations.AddField(
            model_name='movie',
            name='videos',
            field=models.ManyToManyField(to='core.Video'),
        ),
    ]