# Generated by Django 3.1.3 on 2021-04-02 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taxi_Manager', '0017_auto_20210402_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='taxi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Taxi_Manager.taxi'),
        ),
    ]
