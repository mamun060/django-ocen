from django import forms
from django.contrib.auth.models import User, Group

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'groups']

class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
