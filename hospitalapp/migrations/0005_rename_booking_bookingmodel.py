# Generated by Django 4.1.2 on 2022-11-07 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='booking',
            new_name='bookingmodel',
        ),
    ]
