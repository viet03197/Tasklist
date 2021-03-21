from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import UserForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = UserForm(request.POST)
        print(request.POST)
        if register_form.is_valid():
            messages.success(request, "Registered Successfully!")
            register_form.save()
            return redirect('register')
    register_form = UserForm()
    return render(request, 'register.html', {'register': register_form})