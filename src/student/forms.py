from django import forms
from company.models import JobOffer, InternshipOffer
from accounts.models import Resume, StudentProfile
from django.conf import settings


class JobOfferForm(forms.ModelForm):
    resume = forms.ModelChoiceField(queryset=Resume.objects.none(), empty_label='Select Resume')

    def __init__(self, user, *args, **kwargs):
        super(JobOfferForm, self).__init__(*args, **kwargs)
        resumes = Resume.objects.filter(student__user=user, is_verified=True)
        self.fields['resume'].queryset = resumes

    class Meta:
        model = JobOffer
        fields = ('profile', 'student', 'resume',)


class InternshipOfferForm(forms.ModelForm):
    resume = forms.ModelChoiceField(queryset=Resume.objects.none(), empty_label='Select Resume')

    def __init__(self, user, *args, **kwargs):
        super(InternshipOfferForm, self).__init__(*args, **kwargs)
        resumes = Resume.objects.filter(student__user=user, is_verified=True)
        self.fields['resume'].queryset = resumes

    class Meta:
        model = InternshipOffer
        fields = ('profile', 'student', 'resume',)


class StudentDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = (
            'roll_no', 'gpa', 'ug_gpa', 'phone', 'dob', 'category', 'jee_air',
            'x_year', 'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage',
            'current_address', 'permanent_address', 'nationality', 'physical_disability',
        )
    roll_no = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    gpa = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    ug_gpa = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    x_year = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    x_board_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    x_percentage = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    xii_year = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    xii_board_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    xii_percentage = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))

    if(settings.CHANGE_GPA):
        gpa.widget.attrs['readonly'] = False
        ug_gpa.widget.attrs['readonly'] = False
    else:
        gpa.widget.attrs['readonly'] = True
        ug_gpa.widget.attrs['readonly'] = True
