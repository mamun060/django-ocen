from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('login/', views.view_login , name="login"),
    path('register/', views.register_view , name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.dashboard , name='dashboard'),
]
