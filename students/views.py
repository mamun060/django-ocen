# myapp/views.py
from django.shortcuts import render, redirect
from .models import Student
from django.template import loader
from django.http import HttpResponse

def students(request):
    mystudents = Student.objects.all()  # Fetch all members
    context = {
        'mystudents': mystudents,
    }
    return render(request, 'students.html', context)


# create student def
def createStudent(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # Create and save the new Student instance
        Student.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            address=address
        )
        return redirect('students')  # Redirect to the student list page

    return render(request, 'create_student.html')


# student details def 
def details(request, id):
    student = Student.objects.get(id=id)
    template = loader.get_template('student_details.html')
    context = {
        'student': student,
    }
    return HttpResponse(template.render(context, request))

# delete student
def delete_student(request , id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')

# udpate student
def udpate_student(request, id):
    student = Student.objects.get(id=id)
    if( request.method == 'POST'):
        student.firstName = request.POST.get('firstName')
        student.lastName = request.POST.get('lastName')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.save()  # Save the updated student details
        return redirect('students')
    
    context = {
        'student': student
    }
    return render(request, 'update_student.html', context)