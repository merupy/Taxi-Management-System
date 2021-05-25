from . import views 
from .views import (
    DriverChartView, DriverList, DriverRecordView, PasswordChange, TaxiList, drowAPI, loginPage, taxi_registration_view, TaxiDetailView, ViewDriverDetail, TaxiUpdateView, TaxiDelete ,welcome , LoginView, LogoutView, DriverDrowsinessView,
    DriverDelete,
    DriverUpdateView
)
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

app_name = 'Taxi_Manager'
urlpatterns = [
    path('', views.loginPage, name='Login'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logoutUser, name='Logout'),
    path('welcome/', views.welcome, name='welcome'),


    path('driver/', views.driverhome, name='drowsiness'),
    

    path('register/taxi/', views.taxi_registration_view, name='register-taxi'),
    path('view/taxi/', views.TaxiList.as_view(), name='view-taxi'),
    path('view/taxi/<int:pk>/',views.TaxiDetailView.as_view(), name='taxi-detail'),
    path('view/taxi/<int:pk>/update/',views.TaxiUpdateView.as_view(), name='update-taxi'),
    path('view/taxi/<int:pk>/delete/',views.TaxiDelete.as_view(), name='delete-taxi'),

    path('register/driver/', views.driver_registration_view, name='register-driver'),
    path('view/driver/', views.DriverList.as_view(), name='view-driver'),
    path('view/driver/<int:pk>',views.ViewDriverDetail.as_view(), name='driver-detail'),
    path('view/driver/<int:pk>/update/',views.DriverUpdateView.as_view(), name='update-driver'),
    path('view/driver/<int:pk>/delete/',views.DriverDelete.as_view(), name='delete-driver'),

    path('add/income/', views.add_income_view, name='add-income'),
    path('view/income', views.total_price, name='view-income'),
    path('view/income/<int:pk>',views.IncomeDetailView.as_view(), name='income-detail'),
    path('view/income/<int:pk>/update/',views.IncomeUpdateView.as_view(), name='update-income'),
    path('view/income/<int:pk>/delete/',views.IncomeDelete.as_view(), name='delete-income'),

    path('drowsiness/', views.drowiness, name='drowsiness'),

    path('api/drow/', drowAPI.as_view(), name='drow'),

    path('api/driver', DriverRecordView.as_view(), name='drivers'),
    
    path('api/driver_login', LoginView.as_view(), name='driver_login'),

    path('api/driver_logout', LogoutView.as_view(), name='driver_logout'),
    
    path('api/driver_drowsiness', DriverDrowsinessView.as_view(), name='driver_drowsiness'),

    path('charts/patient/', DriverChartView.as_view(), name='driver-chart'),

    path('ajax/driver_age_chart/', views.driver_age_chart, name='driver-age-chart'),
    path('ajax/driver_gender_chart/', views.driver_gender_chart, name='driver-gender-chart'),

    path('account/password_change/', PasswordChange.as_view(), name='password-change'),
    path('account/password_change_complete/', views.password_change_complete, name='password-change-complete'),
]