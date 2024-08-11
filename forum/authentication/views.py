from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

def log_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, "There was an error logging in. Try again...")
            return redirect('log_user')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/')
