from enum import unique
from django import forms
from django.contrib.auth import models
from django.forms import ModelForm
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from .models import Owner, Taxi, Driver, Income
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
         model = User
         fields = ('username', 'password')

class TaxiRegistrationForm(forms.Form):
    taxi_no = forms.CharField(label='Taxi No', required=True)
    registration_date = forms.DateField(
              widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    next_servicing_date = forms.DateField(
              widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    brand = forms.CharField(label='Brand Name', required=True)
    next_tax_payment_date = forms.DateField(
            widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )

class DriverRegistrationForm(forms.Form):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not to Specify', 'Not to Specify'),
    ]
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    gender = forms.ChoiceField(choices=GENDER)
    date_of_birth = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    salary = forms.IntegerField(label='Salary', required=True)
    taxi = forms.ModelChoiceField(queryset=Taxi.objects.all(), required=True)
    joined_date = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )

    termination_date = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    contact_no = forms.IntegerField(required=True, error_messages={'invalid': 'Your email address is incorrect'})
    email = forms.EmailField(required=True)
    country = forms.CharField(label='Country',required=True)
    state = forms.CharField(label='State',required=True)
    district = forms.CharField(label='District',required=True)
    city = forms.CharField(label='City',required=True)


class DailyIncomeForm(forms.Form):
    taxi = forms.ModelChoiceField(queryset=Taxi.objects.all(), required=True)
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), required=True)
    daily_income = forms.IntegerField(label='Daily Income',required=True)
    registration_date = forms.DateField(
              widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    start_trip = forms.FloatField(label='Start Trip', required=True)
    end_trip = forms.FloatField(label='End Trip', required=True)