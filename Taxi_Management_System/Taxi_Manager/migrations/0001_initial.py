# Generated by Django 3.1.3 on 2021-03-28 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not to Specify', 'Not to Specify')], max_length=14)),
                ('date_of_birth', models.DateField()),
                ('salary', models.CharField(max_length=10)),
                ('joined_date', models.DateField()),
                ('termination_date', models.DateField()),
                ('contact_no', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_no', models.CharField(max_length=10)),
                ('registration_date', models.DateField()),
                ('next_servicing_date', models.DateField()),
                ('brand', models.CharField(max_length=50)),
                ('next_tax_payment_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_income', models.IntegerField()),
                ('registration_date', models.DateField()),
                ('start_trip', models.FloatField()),
                ('end_trip', models.FloatField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.driver')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='Drowsiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('Time', models.TimeField(null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.driver')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='taxi_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Taxi_Manager.taxi'),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
