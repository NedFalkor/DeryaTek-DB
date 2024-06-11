# Generated by Django 5.0.2 on 2024-05-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt_bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandmember',
            name='band_member_instrument',
            field=models.CharField(choices=[('All Instruments', 'All Instruments'), ('Bass', 'Bass'), ('Drums', 'Drums'), ('Guitars', 'Guitars'), ('Programming', 'Programming'), ('Synthesizer', 'Synthesizer'), ('Violin', 'Violin'), ('Vocals', 'Vocals')], max_length=50),
        ),
    ]
