from django.shortcuts import render , redirect
from .models import Teacher
from django.template import loader
from django.http import HttpResponse , HttpResponseForbidden
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def teachers(request):
    if not request.user.groups.filter(name='Teacher').exists():
        return HttpResponseForbidden("You do not have access to this page.")
    myteachers = Teacher.objects.all()  # Fetch all members
    context = {
        'myteachers': myteachers,
    }
    return render(request, 'teachers.html', context)


# create student def
def createTeacher(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Create and save the new Student instance
        Teacher.objects.create(
            firstname = firstname,
            email = email,
            phone = phone,
            address = address
        )
        # return redirect('teachers')  # Redirect to the student list page
    
    return render(request, 'create_teacher.html')


# student details def 
def details_teahcer(request, id):
    teacher = Teacher.objects.get(id=id)
    template = loader.get_template('teacher_details.html')
    context = {
        'teacher': teacher,
    }
    return HttpResponse(template.render(context, request))

# delete student
def delete_teacher(request , id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('students')

# udpate student
def udpate_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if( request.method == 'POST'):
        teacher.firstname = request.POST.get('firstname')
        teacher.email = request.POST.get('email')
        teacher.phone = request.POST.get('lastName')
        teacher.address = request.POST.get('address')
        teacher.save()  # Save the updated student details
        return redirect('students')
    
    context = {
        'teacher': teacher
    }
    return render(request, 'update_student.html', context)