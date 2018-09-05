from django import forms
from django.contrib.auth.models import User
from .models import Resume
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile, StudentProfile
from student.models import ProgramAndBranch


class ResumeForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Resume
        fields = ('file', 'reference', 'student')


class StudentRegisterForm(UserCreationForm):
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
    username = forms.CharField(max_length=9, help_text="Enter your Roll number, this will be used to login")
    year = forms.IntegerField(max_value=5, help_text="Enter value between 1-5, the current year of your degree")
    program_branch = forms.ChoiceField(choices=ProgramAndBranch.objects.values_list('abbreviation', 'name'))
    gpa = forms.FloatField(max_value=10.00)
    phone = forms.CharField(max_length=15)
    dob = forms.DateField()
    category = forms.ChoiceField(choices=StudentProfile.CATEGORY)
    jee_air = forms.IntegerField()
    physical_disability = forms.BooleanField(required=False)
    nationality = forms.ChoiceField(choices=StudentProfile.NATION)
    permanent_address = forms.CharField(widget=forms.Textarea)
    current_address = forms.CharField(widget=forms.Textarea)
    x_year = forms.IntegerField(max_value=2050, min_value=2000)
    x_board_name = forms.CharField(max_length=100)
    x_percentage = forms.CharField(max_length=10)
    xii_year = forms.IntegerField(max_value=2050, min_value=2000)
    xii_board_name = forms.CharField(max_length=100)
    xii_percentage = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


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
