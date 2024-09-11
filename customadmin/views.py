from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
# provide authorization 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def groupView(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        group_name = request.POST.get('group_name')
        
        # Fetch the user and group objects
        user = User.objects.get(id=user_id)
        group = Group.objects.get(name=group_name)
        
        # Add the user to the specified group
        user.groups.add(group)
        
        # Return a response to indicate success
        return HttpResponse(f"User {user.username} added to group {group_name}")

    # Fetch all users and groups to display in the form
    users = User.objects.all()
    groups = Group.objects.all()

    return render(request, 'groups/group_assign.html', {'users': users, 'groups': groups})

@login_required
def group_list(request):
    groups = Group.objects.all()  # Fetch all groups
    return render(request, 'groups/groups.html', {'groups': groups})


@login_required
def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group = Group(name=group_name)
        group.save()  # Create the new group

        # Add permissions to the group if selected
        permissions = request.POST.getlist('permissions')
        group.permissions.set(Permission.objects.filter(codename__in=permissions))
        
        return redirect('groups:groups')  # Redirect to group list view

    permissions = Permission.objects.all()  # Fetch all permissions
    return render(request, 'groups/group_create.html', {'permissions': permissions})


@login_required
def group_update(request, group_id):
    group = Group.objects.get(id=group_id)

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group.name = group_name
        group.save()

        # Update permissions
        permissions = request.POST.getlist('permissions')
        group.permissions.set(Permission.objects.filter(codename__in=permissions))
        
        return redirect('group_list')  # Redirect back to the group list

    permissions = Permission.objects.all()  # Fetch all permissions
    group_permissions = group.permissions.values_list('codename', flat=True)
    return render(request, 'groups/group_update.html', {
        'group': group, 
        'permissions': permissions, 
        'group_permissions': group_permissions
    })


@login_required
def group_delete(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()  # Delete the group
    return redirect('group_list')

# Permission management view
@login_required
def permissionView(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        permission_codenames = request.POST.getlist('permissions')  # Get a list of selected permissions
        
        # Fetch the user object
        user = User.objects.get(id=user_id)

        # Fetch all selected permission objects
        permissions = Permission.objects.filter(codename__in=permission_codenames)
        
        # Add all selected permissions to the user
        user.user_permissions.add(*permissions)
        
        # Return a response to indicate success
        return HttpResponse(f"Permissions granted to user {user.username}")

    # Fetch all users and permissions to display in the form
    users = User.objects.all()
    permissions = Permission.objects.all()

    return render(request, 'permission/permission.html', {'users': users, 'permissions': permissions})


#Assign group to the user 
def assign_group_to_user(user_id, group_name):
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)


# Create user registration 
@login_required(login_url="/user/login")
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("customadmin:dashboard")
    else:
        form = UserCreationForm()
        return render(request, "user/register.html", { "form": form })


# Login function
def view_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else: 
        form = AuthenticationForm()
    return render(request, "user/login.html", { "form": form })

# Logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")