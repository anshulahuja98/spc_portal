from django import forms
from django.contrib.auth.models import User
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('file', 'reference',)


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
