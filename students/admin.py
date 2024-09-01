from django.contrib import admin
from .models import Student

# Admin Dashboard listed page
class studentAdmin(admin.ModelAdmin):
    list_display = ("firstName" , "lastName" , "email" , "address")

# Register your models here.
admin.site.register(Student , studentAdmin) 