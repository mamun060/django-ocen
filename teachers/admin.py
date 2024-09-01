from django.contrib import admin
from .models import Teacher

# Register your models here.
class teacherAdmin(admin.ModelAdmin):
    list_display = ("firstname" , "email" , "phone" , "address")

admin.site.register(Teacher , teacherAdmin)