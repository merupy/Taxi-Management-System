# Generated by Django 3.1.3 on 2021-04-13 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taxi_Manager', '0020_auto_20210413_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drow',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.driver'),
        ),
    ]
