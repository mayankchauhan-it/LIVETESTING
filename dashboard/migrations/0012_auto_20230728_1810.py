# Generated by Django 3.2.16 on 2023-07-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_onewaybooking_pickup_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='localbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('user_email', models.CharField(max_length=255, null=True)),
                ('pickuplocation', models.CharField(max_length=255, null=True)),
                ('hour', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='roundbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('user_email', models.CharField(max_length=255, null=True)),
                ('pickuplocation', models.CharField(max_length=255, null=True)),
                ('dropofflocation', models.CharField(max_length=255, null=True)),
                ('pickup_date', models.CharField(max_length=255, null=True)),
                ('pickup_time', models.CharField(max_length=255, null=True)),
                ('dropoff_date', models.CharField(max_length=255, null=True)),
                ('dropoff_time', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='formdata',
        ),
        migrations.AddField(
            model_name='onewaybooking',
            name='pickup_time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
