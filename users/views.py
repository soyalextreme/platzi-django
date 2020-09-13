""" User views for the app """

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# models
from django.contrib.auth.models import User
from users.models import Profile

# exceptions
from django.db.utils import IntegrityError

# Create your views here.


def login_view(request):
    """ Login for the user """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("feed")
        else:
            return render(request, 'users/login.html',
                          {"error": "Invalid username and password"})
    return render(request, 'users/login.html')


@login_required
def update_profile(request):
    """ Updates a /users/loginusers profile view """
    return render(request, 'users/update_profile.html')


def signup_view(request):
    """ Register a user in the DB and the plataform """
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['password']
        confirmation_passwd = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if passwd != confirmation_passwd:
            # validacion de contrasenas diferentes
            error = {'msg':'Password Dont Macth'}
            return render(request, 'users/signup.html', error)
        # creando el usuario base 
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            error = {'msg': 'Username is already picked'}
            return render(request, 'users/signup.html', error)

        # asignamos los datos
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        # Inicializando el profile y le pasamos el user
        profile = Profile(user=user)
        profile.save()
        print('user saved')

        return redirect("login")


    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect("login")
