from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("user/", include("customadmin.urls") ),
    path("", include("students.urls")),
    path("", include("teachers.urls")),
    path('admin/', admin.site.urls),
]
