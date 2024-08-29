# myapp/views.py
from django.shortcuts import render, redirect
from .models import Student

def students(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # Create and save the new Member instance
        Student.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            address=address
        )
        return redirect('students')  # Redirect to the same page or another page

    mystudents = Student.objects.all()  # Fetch all members
    context = {
        'mystudents': mystudents,
    }
    return render(request, 'students.html', context)
