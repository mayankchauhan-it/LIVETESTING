# Generated by Django 3.2.16 on 2023-07-26 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_formdatatest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderupdate',
            name='image',
        ),
    ]
