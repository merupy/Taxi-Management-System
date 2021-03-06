# Generated by Django 3.1.3 on 2021-04-13 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taxi_Manager', '0019_drow_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='taxi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.taxi'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='drivers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.driver'),
        ),
    ]
