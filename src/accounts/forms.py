from django import forms
from django.contrib.auth.models import User
from .models import Resume
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile


class ResumeForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Resume
        fields = ('file', 'reference', 'student')


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class CompanyRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter the same password as before, for verification.',
    )
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'maxlength': '254'}),
        help_text="This Email ID will be your username")
    name = forms.CharField(max_length=50, help_text="Name of the company")
    domain = forms.CharField(max_length=15, help_text="Type of company like banking/consulting etc ")
    url = forms.URLField()
    city = forms.CharField(max_length=15)
    state = forms.CharField(max_length=15)
    country = forms.ChoiceField(choices=CompanyProfile.NATION)
    pin_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
