from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.shortcuts import redirect 
from django.http import HttpResponseRedirect
from django.urls import reverse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Taxi_Manager:home')
        
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_owner(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper_func
    return decorator


def all_login(view_func):
    def wrapper_function (request, *args, **kwargs):
        group = None 
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Drivers':
            return redirect ('Taxi_Manager:drowsiness')

        if group == 'Owners':
            return view_func(request, *args, **kwargs)

        if User.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
    return wrapper_function