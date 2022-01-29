from django.shortcuts import render, redirect
from datetime import datetime
from mapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.


# username: prajx pass: aryanisgreat2003

def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name, email = email, phone = phone, date = datetime.today())
        contact.save()
        messages.success(request, 'Contact details saved successfully.')
    return render(request, 'contact.html')

def register(request): 
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user+' successfully.')
            return redirect('login')
        

    context = {'form': form}
    return render(request,  'register.html', context)

#loginpage

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            messages.info(request, 'Username or Password is incorrect. Please Try Again.')
    context = {}
    return render(request, 'login.html', context)
