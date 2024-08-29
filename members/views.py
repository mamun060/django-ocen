# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
# from .models import Member
# from .forms import MemberForm

# # Create your views here.
# def members(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             form = MemberForm()
#     # mymembers = Member.objects.get().values()
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('index.html')
#     context = {
#         'mymembers': mymembers,
#         'form': form
#     }
#     return HttpResponse(template.render(context, request))


# myapp/views.py
# from django.shortcuts import render, redirect
# from .forms import MemberForm
# from .models import Member

# def member_list(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the same page or a success page
#     else:
#         form = MemberForm()

#     members = Member.objects.all()  # Fetch all members
#     return render(request, 'ind.html', {'form': form, 'mymembers': members})

from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

def members(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm()
    
    # Fetch all members
    mymembers = Member.objects.all()

    # Render the template with context
    context = {
        'mymembers': mymembers,
        'form': form
    }
    return render(request, 'index.html', context)
