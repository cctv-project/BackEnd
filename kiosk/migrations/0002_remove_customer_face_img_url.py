# Generated by Django 3.2.9 on 2021-12-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='face_img_url',
        ),
    ]