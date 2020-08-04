from django import forms
from django.contrib.auth.models import User
from .models import Resume
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile, StudentProfile
from student.models import ProgramAndBranch
from .validators import (
    validate_year, validate_gpa, validate_domain, validate_url, validate_pincode, check_file_size, regex_validators)


class ResumeForm(forms.ModelForm):
    file = forms.FileField(validators=[check_file_size, ])

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
    username = forms.CharField(max_length=11, help_text="Enter your Roll Number, this will be used to login",
                               label="Username",
                               validators=[regex_validators],
                               required=True)
    year = forms.IntegerField(max_value=10, help_text="Enter value between 1-5, the current year of your degree",
                              label="Current Year Of Degree",
                              validators=[validate_year])
    program_branch = forms.ModelChoiceField(queryset=ProgramAndBranch.objects.all(), label="Program Branch")
    gpa = forms.FloatField(max_value=10.00, label="GPA", validators=[validate_gpa])
    ug_gpa = forms.FloatField(max_value=10.00, required=False, label="U.G. GPA", validators=[validate_gpa])
    phone = forms.CharField(max_length=15, label="Phone")
    dob = forms.DateField(required=True, label="Date Of Birth", widget=forms.SelectDateWidget(years=range(1960, 2020)))
    category = forms.ChoiceField(choices=StudentProfile.CATEGORY, label="Category")
    jee_air = forms.IntegerField(required=False, label="JEE AIR")
    physical_disability = forms.BooleanField(required=False, label="Physical Disability")
    nationality = forms.ChoiceField(choices=StudentProfile.NATION, label="Nationality")
    permanent_address = forms.CharField(widget=forms.Textarea, label="Permanent Address")
    current_address = forms.CharField(widget=forms.Textarea, label="Current Address")
    x_year = forms.IntegerField(max_value=2050, min_value=1980, label="10th Board Year")
    x_board_name = forms.CharField(max_length=100, label="10th Board Name")
    x_percentage = forms.CharField(max_length=10, label="10th Percentage")
    xii_year = forms.IntegerField(max_value=2050, min_value=1980, label="12th Board Year")
    xii_board_name = forms.CharField(max_length=100, label="12th Board Name")
    xii_percentage = forms.CharField(max_length=16, label="12th Percentage")
    std_image = forms.ImageField(required=True, label="Upload your image", validators=[check_file_size, ])

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.endswith('@iitj.ac.in') is False:
            raise forms.ValidationError("Enter the IITJ email id.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']
        required = (
            'last_name',
            'email',
        )


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
        label="The Email ID will be your username")
    name = forms.CharField(max_length=50, help_text="Name of the company", label="Name of the company")
    domain = forms.CharField(
        max_length=15,
        help_text="Type of company like banking/consulting etc ",
        required=False,
        label="Domain (Type of company like banking/consulting etc)",
        validators=[validate_domain])
    url = forms.CharField(
        required=False,
        label="Enter the URL of your company's website",
        help_text="(Must start with https/http)",
        validators=[validate_url])
    city = forms.CharField(max_length=15, required=False, label="City")
    state = forms.CharField(max_length=15, required=False, label="State")
    country = forms.ChoiceField(choices=CompanyProfile.NATION, label="Country")
    pin_code = forms.CharField(max_length=10, required=False, label="Pin Code", validators=[validate_pincode])
    contact = forms.CharField(max_length=20, required=True, label="Contact Number")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
