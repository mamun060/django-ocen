from django.contrib import admin
from django.urls import path , include
from customadmin.views import view_login , dashboard , logout_view

urlpatterns = [
    path("", view_login , name="login"),
    path("dashboard/", dashboard , name="dashboard"),
     path('logout/', logout_view, name="logout"),
    path("", include("customadmin.urls") ),
    path("", include("students.urls")),
    path("", include("teachers.urls")),
    path('admin/', admin.site.urls),
]
