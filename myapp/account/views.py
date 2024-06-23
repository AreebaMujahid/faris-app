from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError


# Custom UserCreationForm
class Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


def signup(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                form.add_error(None, 'A user with that username already exists.')
    else:
        form = Form()
    return render(request, 'registration/signup.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def about(request):
    return render(request, 'about.html', {'title': 'About'})