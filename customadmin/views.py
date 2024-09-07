from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

# Create user registration 
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("customadmin:dashboard")
    else:
        form = UserCreationForm()
        return render(request, "user/register.html", { "form": form })


# Login function
def view_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("customadmin:dashboard")
    else: 
        form = AuthenticationForm()
    return render(request, "user/login.html", { "form": form })

# Logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:login")