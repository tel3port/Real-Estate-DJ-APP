# Generated by Django 2.2.16 on 2020-10-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='keywords',
            field=models.TextField(blank=True),
        ),
    ]