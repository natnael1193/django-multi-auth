import django
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if not request.user.is_authenticated:
        msg = None
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                msg = 'User Created'
                return redirect('login_view')
            else:
                msg = "Form is not valid"
        else:
            form = SignUpForm()
        return render(request, 'auth/registration.html', {'form': form, 'msg': msg})
    else:
        return redirect('index')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = LoginForm(request.POST or None)
        msg = None

        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None and user.is_admin:
                    login(request, user)
                    return redirect('admin')
                elif user is not None and user.is_customer:
                    login(request, user)
                    return redirect('customer')
                elif user is not None and user.is_employee:
                    login(request, user)
                    return redirect('employee')
                else:
                    msg = 'invalid credentials'
            else:
                msg = 'error validating form'
    return render(request, 'auth/login.html', {'form': form, 'msg': msg})


@login_required(login_url='/login_view/')
def profile(request):
    return render(request, 'auth/profile.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required(login_url='/login_view/')
def home(request):
    if request.user.is_admin:
        return render(request, 'home.html')
    else:
        return redirect('index')


@login_required(login_url='/login_view/')
def admin(request):
    return render(request, 'admin.html')


@login_required(login_url='/login_view/')
def customer(request):
    return render(request, 'customer.html')


@login_required(login_url='/login_view/')
def employee(request):
    return render(request, 'employee.html')

def not_authenticated(request):
    return render(request, 'auth/not_authenticated.html')