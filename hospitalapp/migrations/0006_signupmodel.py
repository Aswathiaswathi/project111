# Generated by Django 4.1.2 on 2022-11-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_rename_booking_bookingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('re_password', models.CharField(max_length=10)),
            ],
        ),
    ]
