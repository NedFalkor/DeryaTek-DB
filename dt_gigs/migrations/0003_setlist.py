# Generated by Django 5.0.2 on 2024-06-11 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt_gigs', '0002_rename_address_venue_venue_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_number', models.IntegerField()),
                ('song_title', models.CharField(max_length=255)),
                ('song_duration', models.DurationField(blank=True, null=True)),
                ('album_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setlist', to='dt_gigs.gig')),
            ],
            options={
                'ordering': ['song_number'],
                'unique_together': {('gig', 'song_number')},
            },
        ),
    ]
