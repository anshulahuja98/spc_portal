from django import forms
from django.contrib.auth.models import User
from .models import Resume
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile, StudentProfile
from student.models import ProgramAndBranch
from django.core.validators import RegexValidator


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
    username = forms.CharField(max_length=11, help_text="Enter your Roll number, this will be used to login",
                               label="Username",
                               validators=[RegexValidator(r'[A-Z]([A-Z]?)[0-9]{2}([A-Z]?)([A-Z]?)([A-Z]?)[0-9]{3}'
                                                          r'([0-9]?){4}',
                                                          "Enter your Roll number(in correct "
                                                          "format like eg. B17CS006 ). "
                                                          "This will be used to login ")],
                               required=True)
    year = forms.IntegerField(max_value=10, help_text="Enter value between 1-5, the current year of your degree",
                              label="Current Year Of Degree")
    program_branch = forms.ModelChoiceField(queryset=ProgramAndBranch.objects.all(), label="Program Branch")
    gpa = forms.FloatField(max_value=10.00, label="GPA")
    ug_gpa = forms.FloatField(max_value=10.00, required=False, label="U.G. GPA")
    phone = forms.CharField(max_length=15, label="Phone")
    dob = forms.DateField(required=True, label="Date Of Birth", widget=forms.SelectDateWidget())
    email = forms.EmailField(required=True)
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
    std_image = forms.ImageField(required=True, label="Upload your image")

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
    domain = forms.CharField(max_length=15, help_text="Type of company like banking/consulting etc ", required=False,
                             label="Domain(Type of company like banking/consulting etc)")
    url = forms.CharField(required=False, label="Enter the URL of your company's website")
    city = forms.CharField(max_length=15, required=False, label="City")
    state = forms.CharField(max_length=15, required=False, label="State")
    country = forms.ChoiceField(choices=CompanyProfile.NATION, label="Country")
    pin_code = forms.CharField(max_length=10, required=False, label="Pin Code")
    contact = forms.CharField(max_length=20, required=True, label="Contact Number")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
