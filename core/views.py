from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                # For Security Purposes
                messages.info(request, 'Email or User Name Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                # For Security Purposes
                messages.info(request, 'Email or User Name Already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                # Log the user in and redirect to settings page
                # Create a Profile object for the new user
                # user_model = User.objects.get(username=username)
                # new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile = Profile.objects.create(
                    user=user, id_user=user.id)
                new_profile.save()
                return redirect('signup')  # should be the login page

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):

    auth.logout(request)
    return redirect('signin')
