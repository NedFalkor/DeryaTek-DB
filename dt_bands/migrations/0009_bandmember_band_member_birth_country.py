# Generated by Django 5.0.2 on 2024-06-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt_bands', '0008_band_band_separation_date_band_band_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandmember',
            name='band_member_birth_country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
