# Generated by Django 5.0.2 on 2024-05-07 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dt_genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_member_name', models.CharField(max_length=100)),
                ('band_member_birth_year', models.IntegerField()),
                ('band_member_country', models.CharField(max_length=100)),
                ('band_member_instrument', models.CharField(choices=[('Bass', 'Bass'), ('Guitars', 'Guitars'), ('Drums', 'Drums'), ('Vocals', 'Vocals'), ('Synthesizer', 'Synthesizer')], max_length=50)),
                ('band_member_photo', models.ImageField(blank=True, null=True, upload_to='member_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=100)),
                ('band_country', models.CharField(max_length=100)),
                ('band_formed_in', models.IntegerField()),
                ('band_description', models.TextField()),
                ('band_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='dt_genres.genre')),
                ('band_members', models.ManyToManyField(related_name='members', to='dt_bands.bandmember')),
            ],
        ),
    ]
