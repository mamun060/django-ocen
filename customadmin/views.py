from django.shortcuts import render , redirect
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate , login


# Create your views here.
def dashboardView(request):
    return render(request, 'dashboard.html')