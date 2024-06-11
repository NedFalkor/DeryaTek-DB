# Generated by Django 5.0.2 on 2024-05-14 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt_genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=100)),
                ('style_description', models.TextField()),
                ('style_photo', models.ImageField(blank=True, null=True, upload_to='style_photos/')),
                ('style_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='styles', to='dt_genres.genre')),
            ],
        ),
    ]