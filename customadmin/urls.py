from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    # path('login/', views.view_login , name="login"),
    path('user/register/', views.register_view , name="register"),
    path('user/permission/', views.permissionView, name="permission"),
    path('user/groups/', views.groupView, name="groups")
]
