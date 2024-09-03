from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('members.urls')),
    path('', include('students.urls')),
    path('', include('teachers.urls')),
    path('', include('customadmin.urls')),
    path('admin/', admin.site.urls),
]
