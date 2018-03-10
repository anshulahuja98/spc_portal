from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
from .models import CompanyProfile


class CompanyRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'maxlength': '254'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_last_name(self):
        _dict = super(RegisterForm, self).clean()
        return _dict['last_name'].capitalize()

    def clean_email(self):
        if User.objects.filter(email__iexact=self.data['email']).exists():
            raise forms.ValidationError('This email is already registered')
        return self.data['email']


class StudentRegisterForm(UserCreationForm):

    rollno = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '254'}))

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_last_name(self):
        _dict = super(RegisterForm, self).clean()
        return _dict['last_name'].capitalize()

    def clean_email(self):
        if User.objects.filter(email__iexact=self.data['email']).exists():
            raise forms.ValidationError('This email is already registered')
        return self.data['email']
