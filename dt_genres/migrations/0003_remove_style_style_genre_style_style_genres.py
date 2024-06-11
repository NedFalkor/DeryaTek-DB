# Generated by Django 5.0.2 on 2024-06-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt_genres', '0002_style'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='style_genre',
        ),
        migrations.AddField(
            model_name='style',
            name='style_genres',
            field=models.ManyToManyField(related_name='styles', to='dt_genres.genre'),
        ),
    ]