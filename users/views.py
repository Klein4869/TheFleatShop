from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm, RegistForm
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def register(request):
    loginForm = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        errors = []

        registerForm = RegistForm(
            {'username': username, 'password': password, 're_password': re_password, 'email': email})
        if not registerForm.is_valid():
            return render(request, 'account.html', {'registForm': registerForm, 'loginForm': loginForm})
        if password != re_password:
            errors.append('两次密码不一致')
            return render(request, 'account.html',
                          {'registForm': registerForm, 'errors': errors, 'loginForm': loginForm})

        filterResult = User.objects.filter(username=username)
        if len(filterResult) > 0:
            errors.append('用户名已存在')
            return render(request, 'account.html',
                          {'registForm': registerForm, 'errors': errors, 'loginForm': loginForm})

        emailfilter = User.objects.filter(email=email)
        if len(emailfilter) > 0:
            errors.append('邮箱已被使用')
            return render(request, 'account.html',
                          {'registForm': registerForm, 'errors': errors, 'loginForm': loginForm})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        newUser = auth.authenticate(request, username=username, password=password)
        if newUser is not None:
            auth.login(request, newUser)
            return render(request, 'index.html', {'username':username})
        else:
            return render(request, 'account.html',
                          {'registForm': registerForm, 'errors': errors, 'loginForm': loginForm})
    else:
        loginForm = LoginForm()
        registerForm = RegistForm()
        return render(request, 'account.html', {'registForm': registerForm, 'loginForm': loginForm})


def login(request):
    registForm = RegistForm()
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'account.html', {'loginForm': loginForm, 'registForm': registForm})
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        loginForm = LoginForm(
            {'username': username,
             'password': password,})
        if not loginForm.is_valid():
            return render(request, 'index.html', {'registForm': registForm, 'loginForm': loginForm})
        else:
            user = auth.authenticate(request, username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return render(request, 'index.html', {'username': user.username})
            else:
                print(user)
                return render(request, 'account.html',
                                {'loginForm': loginForm, 'password_is_wrong': True, 'registForm': registForm})


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def account(request):
    registerForm = RegistForm()
    loginForm = LoginForm()
    return render(request, 'account.html', {'registForm': registerForm, 'loginForm': loginForm})
