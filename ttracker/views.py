# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


def home(request):
    return render(request, 'pages/home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'pages/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('manager')

            elif user is not None and user.is_employer:
                login(request, user)
                return redirect('employee')
            elif user is not None:
                login(request, user)
                return redirect('employee')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    return render(request, 'pages/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request, 'pages/admin.html')


def employer(request):
    return render(request, 'pages/employee.html')


def logout_user(request):
    logout(request)
    return redirect('login_view')

