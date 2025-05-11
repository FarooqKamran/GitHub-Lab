from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Reservation, MenuItem

def home_view(request):
    return render(request, 'myapp/Home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'myapp/SignUp.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'myapp/Login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def reservations_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        party_size = request.POST['party-size']
        Reservation.objects.create(name=name, phone=phone, email=email, date=date, time=time, party_size=party_size)
        return redirect('reservations')
    party_sizes = range(1, 11)
    return render(request, 'myapp/Reservations.html', {'party_sizes': party_sizes})



def menu_view(request):
    categories = {
        'breakfast': MenuItem.objects.filter(category='breakfast'),
        'lunch': MenuItem.objects.filter(category='lunch'),
        'night': MenuItem.objects.filter(category='night'),
    }
    return render(request, 'myapp/Menu.html', {'categories': categories})
