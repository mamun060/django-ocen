## start Django Role Based permission setup custom admin dashboard

### Django user registration in views file
```python
from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm 

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customadmin:dashboard")
    else:
        form = UserCreationForm()
        # file path name (folder/filename)
        return render(request, "admin/register.html", { "form": form })
```

### register urls.py file
```python
    from django.urls import path
    from . import views
    from django.contrib.auth import views as auth_views

    urlpatterns = [
        path('register/', views.register_view, name="register"),
    ]
```

### register template file
```python
<form method="post" action="/register/">
    #action="/register/" is url 
    <div class="row">
        {% csrf_token %}
        {{ form }}
    </div>
```
### Login user 
    
### Login user viwe
```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

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
```

### url setup for login
```python
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customadmin'

urlpatterns = [
    path('login/', views.view_login , name="login"),
]
```

### template file for login page
```python
    <form action="/login/" method="post" >
        {% csrf_token %}
        {{ form }} 
        <button type="submit" class="btn btn-primary btn-block mt-2">Submit</button>
    </form>
```

### Logout in views file
```python
from django.contrib.auth import logout

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:login")

# Now Need to setup urls
path('logout/', views.logout_view, name="logout")

# setup logout form with button
<form method="post" action="{% url 'user:logout' %}">
    {% csrf_token %}
    <button>
        Logout
    </button>
</form>
```

### Let's start authorization
