from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})
