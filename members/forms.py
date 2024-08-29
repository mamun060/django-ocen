from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstName', 'lastName', 'email', 'address']

        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
        }