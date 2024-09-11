from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    # path('login/', views.view_login , name="login"),
    path('user/register/', views.register_view , name="register"),
    path('user/permission/', views.permissionView, name="permission"),
    path('user/groups/', views.group_list, name="groups"),
    path('user/groups/assign/', views.groupView, name="group_assign"),
    path('user/groups/create/', views.group_create, name='group_create'),
    path('user/groups/update/<int:group_id>/', views.group_update, name='group_update'),
    path('user/groups/delete/<int:group_id>/', views.group_delete, name='group_delete'),
]
