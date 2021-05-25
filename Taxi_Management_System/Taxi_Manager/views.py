from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.core.checks import messages
from django.shortcuts import render, reverse, redirect
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.authtoken.models import Token 
from rest_framework.serializers import ModelSerializer
from .models import Drow, Owner, Taxi, Driver, Income
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import GenericViewError, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import DriverRegistrationForm, TaxiRegistrationForm, DailyIncomeForm
from django.contrib.auth.models import Group, User
from django.db.models import Sum, Count, query
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import all_login, allowed_owner, unauthenticated_user
from django.http import HttpResponse, request
from django.contrib import auth
import datetime
from django.contrib.auth import views as auth_views


# API imports
from rest_framework.views import APIView
from .serializer import DriverSerializer, DrowsinessSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Taxi_Manager:home')

        else:
            messages.error(request, "Username OR password incorrect")

    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('Taxi_Manager:Login')


@login_required(login_url='/')
@all_login
def home_page(request):
    total_drivers = Driver.objects.count()
    total_taxi = Taxi.objects.count()
    content = {'drivers':total_drivers, 'taxi':total_taxi}
    # import pdb
    # pdb.set_trace()
    return render(request, 'Taxi_Manager/index.html', content)

@login_required
def driverhome(request):
    return render(request, 'Taxi_Manager/drowsiness.html')


def welcome(request):
    return render(request, "Taxi_Manager/welcome_page.html")

@login_required(login_url='/')
@allowed_owner(allowed_roles=['Owners'])
def taxi_registration_view(request):
    if request.method == "POST":
        form = TaxiRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_taxi = Taxi(taxi_no=data['taxi_no'],registration_date=data['registration_date'],
                            next_servicing_date=data['next_servicing_date'],
                            brand=data['brand'], next_tax_payment_date=data['next_tax_payment_date']
                            )
            new_taxi.save()
            return redirect('Taxi_Manager:view-taxi')
    else:
        form = TaxiRegistrationForm()
    return render(request,'Taxi_Manager/register_taxi.html',{'form': form})

class TaxiList(ListView):
    model = Taxi
    template_name = 'Taxi_Manager/view_taxi.html'

class TaxiDetailView(DetailView):
    model = Taxi
    template_name = 'Taxi_Manager/view_taxi_detail.html'

class TaxiUpdateView(UpdateView):
    model = Taxi
    fields = ('taxi_no', 'registration_date',
            'next_servicing_date', 'brand',
            'next_tax_payment_date',
            )
    template_name = 'Taxi_Manager/update_taxi_detail.html'
    def get_success_url(self):
        return reverse('Taxi_Manager:view-taxi')

class TaxiDelete(DeleteView):
    model = Taxi
    template_name = 'Taxi_Manager/delete.html'
    success_url = reverse_lazy('Taxi_Manager:view-taxi')

@login_required(login_url='/')
@allowed_owner(allowed_roles=['Owners'])
def driver_registration_view(request):
    if request.method == "POST":
        data = request.POST
        User.objects.create_user(username=data['username'],password=data['password1'],first_name=data['first_name'], last_name=data['last_name'])
        user = User.objects.all().last().id
        user = User.objects.get(id=user)
        new_driver = Driver(user = user,first_name=data['first_name'], last_name=data['last_name'],
                                 gender=data['gender'], date_of_birth=data['date_of_birth'],
                                 #profile_image=data['profile_image'],
                                 salary=data['salary'],
                                 taxi=Taxi.objects.get(id=int(data['taxi'])),
                                 joined_date=data['joined_date'],
                                 termination_date=data['termination_date'], contact_no=data['contact_no'],
                                 email=data['email'], country=data['country'], state=data['state'],
                                 district=data['district'], city=data['city']
                                 )
        new_driver.save()
        group = Group.objects.get(name='Drivers')
        user.groups.add(group)
    user_form = UserCreationForm()
    form = DriverRegistrationForm()
    return render(request, 'Taxi_Manager/register_driver.html', {
        'user_form': user_form,
        'form': form,
        })


class DriverList(ListView):
    model = Driver
    template_name = 'Taxi_Manager/view_driver.html'


class ViewDriverDetail(DetailView):
    model = Driver
    template_name = 'Taxi_Manager/view_driver_detail.html'


class DriverUpdateView(UpdateView):
    model = Driver
    fields = ('first_name', 'last_name',
              'gender', 'date_of_birth', 'salary',
              'joined_date', 'termination_date', 'taxi',
              'contact_no', 'email',
              'country', 'state', 'district', 'city',
              )
    template_name = 'Taxi_Manager/update_driver_detail.html'
    def get_success_url(self):
        return reverse('Taxi_Manager:view-driver')

class DriverDelete(DeleteView):
    model = Driver
    template_name = 'Taxi_Manager/delete.html'
    success_url = reverse_lazy('Taxi_Manager:view-driver')

# class DriverListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = DriverSerializer
#     queryset = Driver.objects.all()

class DriverRecordView(APIView):

    def get(self, request, format=None):
        #print(self.request.user)
        driver_data = Driver.objects.filter(user=self.request.user.id)
        serializer = DriverSerializer(driver_data, many=True)
        return Response(serializer.data)

class DriverDrowsinessView(APIView):
    dpermission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        #print(self.request.user)
        driver_data = Driver.objects.get(user=self.request.user.id)
        drowsiness_data = Drow.objects.filter(driver=driver_data)
        serializer = DrowsinessSerializer(drowsiness_data, many=True)
        return Response(serializer.data)


@login_required(login_url='/')
def add_income_view(request):
    if request.method == "POST":
        form = DailyIncomeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_income = Income(taxi=data['taxi'], driver=data['driver'],
                            daily_income=data['daily_income'],
                            registration_date=data['registration_date'],
                            start_trip=data['start_trip'], end_trip=data['end_trip']
                            )
            new_income.save()
            return redirect('Taxi_Manager:view-income')
    else:
        form = DailyIncomeForm()
    return render(request,'Taxi_Manager/add_daily_income.html',{'form': form})

class IncomeList(ListView):
    model = Income
    template_name = 'Taxi_Manager/totalearning.html'
    # def total(request):
    #     total_price = Income.objects.aggregate(Sum('daily_income'))
    #     return render(request, 'Taxi_Manager/totalearning.html',{'total':total_price})

@login_required(login_url='/')
@allowed_owner(allowed_roles=['Owners'])
def total_price(request):
    incomedata = Income.objects.all()
    total_price = Income.objects.aggregate(Sum('daily_income'))
    context = {'incomedata':incomedata,'total':total_price}
    return render(request,'Taxi_Manager/totalearning.html',context)


class IncomeDetailView(DetailView):
    model = Income
    template_name = 'Taxi_Manager/view_income_detail.html'

class IncomeUpdateView(UpdateView):
    model = Income
    fields = ('taxi', 'driver',
            'daily_income', 'registration_date',
            'start_trip','end_trip'
            )
    template_name = 'Taxi_Manager/update_income_detail.html'
    def get_success_url(self):
        return reverse('Taxi_Manager:view-income')

class IncomeDelete(DeleteView):
    model = Income
    template_name = 'Taxi_Manager/delete.html'
    success_url = reverse_lazy('Taxi_Manager:view-income')

# class DrowsinessList(ListView):
#     model = Drow
#     #x = (Drow.objects.filter(driver = request.user.Driver))
#     template_name = 'Taxi_Manager/drowsiness.html'

# def Drowsinessdata(request):
#     return render(request,'Taxi_Manager/drowsiness.html')

def drowiness(request):
    driver_instance = Driver.objects.get(user=request.user.id)
    drows = Drow.objects.filter(driver = driver_instance)
    context = {
        'drows':drows,
        }
    return render(request, 'Taxi_Manager/drowsiness.html',context)

class drowAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):

         modelzz = Drow.objects.all()
         ModelSerializer = DrowsinessSerializer(modelzz, many=True)

         return Response({'drowsiness':ModelSerializer.data})

    def post(self, request):
        datetime_str = request.data['drow_data']
        data = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
        #print(data)
        name = Driver.objects.get(first_name=request.data['name'])

        new_drow = Drow(drowsiness=data, driver=name)
        # #serializer = DrowsinessSerializer(data=data)
        # print(serializer)
        # print(type(request.data['drow_data']))
        # #serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        # serializer.save()
        new_drow.save()
        return Response(status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        try:
            data = self.request.data
            username = data['username']
            password = data['password']
            print(username, password)
            the_user = auth.authenticate(username=username, password=password)
            #try:is_driver = True;Driver.objects.get(user=the_user)
            #except:is_driver= False
            #print(is_driver)
            if the_user is not None: #and #is_driver
                auth.login(request, the_user)
                print(the_user)
                driver_data = Driver.objects.get(user=self.request.user.id)
                drowsiness_data = Drow.objects.filter(driver=driver_data)
                serializer = DrowsinessSerializer(drowsiness_data, many=True)
                context = {
                    'serilizer':serializer.data
                }
                return Response(context)
            else:
                return Response({'error':'user not auhtneticated'})
        except:
            return Response({'error':'something went wrong at login'})

class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success':'logged out'}, status=status.HTTP_200_OK)
        except:
            return Response({'error':'something went wrong while logging out'})



class AuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        driver_data = Driver.objects.get(user=user.id)
        drowsiness_data = Drow.objects.filter(driver=driver_data)
        serializerr = DrowsinessSerializer(drowsiness_data, many=True)
        token, created = Token.objects.get_or_create(user=user)
        context = {'token': token.key,
                   'user_id': user.id, 
                   'username': user.username,
                   'serilizer': serializerr.data,
                   }
        return Response(context)

class DriverChartView(TemplateView):
    template_name = 'Taxi_Manager/index.html'


def driver_age_chart(request):
    queryset = Driver.objects.all()
    labels = ['20-30', '30-40', '40-50', '50-60']
    a = 0
    b = 0
    c = 0
    d = 0

    for obj in queryset:
        difference = datetime.datetime.now().date() - obj.date_of_birth
        years = round(difference.days/365)

        if 20 < years <= 30:
            a = a + 1
        if 30 < years <= 40:
            b = b + 1
        if 40 < years <= 50:
            c = c + 1
        if 50 < years <= 60:
            d = d + 1

    data = [a, b, c, d,]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def driver_gender_chart(request):
    queryset = Driver.objects.all()
    labels = ['Male', 'Female', 'Transgender']
    m = 0
    f = 0
    t = 0

    for driver in queryset:
        if driver.gender == 'Male':
            m = m + 1
        if driver.gender == 'Female':
            f = f + 1
        if driver.gender == 'Transgender':
            t = t + 1

    data = [m, f, t]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('Taxi_Manager:password-change-complete')


@login_required(login_url="/")
def password_change_complete(request):
    return render(request, 'registration/password_change_complete.html')
