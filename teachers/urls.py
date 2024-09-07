from django.urls import path
from . import views

urlpatterns = [
    path("teachers/",  views.teachers, name='students'),
    path("teachers/create", views.createTeacher, name="create_student"),
    path("teachers/details/<int:id>", views.details_teahcer , name="details_teahcer"),
    path("teachers/update/<int:id>", views.udpate_teacher , name="update_teacher"),
    path("teachers/delete/<int:id>", views.delete_teacher , name="delete_teacher")
]