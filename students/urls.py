from django.urls import path
from . import views

urlpatterns = [
    path("students/",  views.students, name='students'),
    path("students/create", views.createStudent, name="create_student"),
    path("students/details/<int:id>", views.details, name="details"),
    path("students/update/<int:id>", views.udpate_student , name="update_student"),
    path("students/delete/<int:id>", views.delete_student , name="delete_student")
]