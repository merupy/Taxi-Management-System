from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model): #This is the owner table who will use the webapp
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.first_name)

class Taxi(models.Model): #All the taxi are registered my owner
    taxi_no = models.CharField(max_length=10)
    registration_date = models.DateField()
    next_servicing_date = models.DateField()
    brand = models.CharField(max_length=50)
    next_tax_payment_date = models.DateField()

    def __str__(self):
        return '%s' % (self.taxi_no)

class Driver(models.Model): #All the driver are registered my owner 
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not to Specify', 'Not to Specify'),
    )
    taxi = models.ForeignKey(Taxi, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=14, choices=GENDER)
    date_of_birth = models.DateField()
    salary = models.IntegerField()
    joined_date = models.DateField()
    termination_date = models.DateField()
    contact_no = models.BigIntegerField(unique=True, error_messages={'unique':"This phone number has already been registered."})
    email = models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Income(models.Model): #This class stores all the daily income produced by individual drivers
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    daily_income = models.IntegerField()
    registration_date = models.DateField()
    start_trip = models.FloatField()
    end_trip = models.FloatField()

    def __str__(self):
        return '%s' % (self.driver)


class Drow(models.Model): #All the drowsiness data of driver will be stored here
    #driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    drowsiness = models.DateTimeField(null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

