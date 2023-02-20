# Generated by Django 3.1.3 on 2021-03-31 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taxi_Manager', '0005_auto_20210331_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='taxi_no',
        ),
        migrations.AddField(
            model_name='taxi',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.driver'),
        ),
    ]