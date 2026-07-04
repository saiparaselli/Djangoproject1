from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from . forms import RegisterForm
from django.contrib import messages

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

            messages.success(request,'Registration successful!')

            return redirect('login')
        else:
            messages.error(request,"please correct the errors below.")

    else:

        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")

    return render(request, 'login.html')

def user_logout(request):

    logout(request)

    return redirect('login')