from django.db.models import fields
from django.db.models import DateTimeField
from rest_framework import serializers
from .models import Drow, Owner,Driver,Taxi,Income

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','email')

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ('taxi_no','registration_date',
                'next_servicing_date','brand',
                'brand','next_tax_payment_date')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('taxi','driver','daily_income',
                'registration_date','start_date',
                'end_trip')

class DrowsinessSerializer(serializers.ModelSerializer):
    #created = serializers.DateTimeField()

    class Meta:
        model = Drow
        #DateTimeField = 'drowsiness,'
        #fields = 'drowsiness,'
        fields = ['drowsiness']

