# Generated by Django 3.1.3 on 2021-04-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taxi_Manager', '0026_auto_20210421_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='salary',
            field=models.FloatField(max_length=10),
        ),
    ]