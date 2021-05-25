# Generated by Django 3.1.3 on 2021-03-31 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Taxi_Manager', '0003_auto_20210331_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
