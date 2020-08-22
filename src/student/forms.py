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
            'roll_no', 'year', 'gpa', 'ug_gpa', 'phone', 'dob', 'category', 'jee_air',
            'x_year', 'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage',
            'current_address', 'permanent_address', 'nationality', 'physical_disability',
        )
    roll_no = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'color: black;'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    gpa = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    ug_gpa = forms.FloatField(required=False, widget=forms.TextInput(attrs={'style': 'color: black;'}))
    x_year = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    x_board_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    x_percentage = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    xii_year = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    xii_board_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    xii_percentage = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    jee_air = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'style': 'color: black;'}))
    current_address = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))
    permanent_address = forms.CharField(widget=forms.TextInput(attrs={'style': 'color: black;'}))

    if(settings.ALLOW_DETAILS_UPDATE):
        year.widget.attrs['readonly'] = False
        gpa.widget.attrs['readonly'] = False
        ug_gpa.widget.attrs['readonly'] = False
        x_year.widget.attrs['readonly'] = False
        x_board_name.widget.attrs['readonly'] = False
        x_percentage.widget.attrs['readonly'] = False
        xii_year.widget.attrs['readonly'] = False
        xii_board_name.widget.attrs['readonly'] = False
        phone.widget.attrs['readonly'] = False
        dob.widget.attrs['readonly'] = False
        jee_air.widget.attrs['readonly'] = False
        current_address.widget.attrs['readonly'] = False
        xii_percentage.widget.attrs['readonly'] = False
        permanent_address.widget.attrs['readonly'] = False
    else:
        year.widget.attrs['readonly'] = True
        gpa.widget.attrs['readonly'] = True
        ug_gpa.widget.attrs['readonly'] = True
        x_year.widget.attrs['readonly'] = True
        x_board_name.widget.attrs['readonly'] = True
        x_percentage.widget.attrs['readonly'] = True
        xii_year.widget.attrs['readonly'] = True
        xii_board_name.widget.attrs['readonly'] = True
        phone.widget.attrs['readonly'] = True
        dob.widget.attrs['readonly'] = True
        jee_air.widget.attrs['readonly'] = True
        current_address.widget.attrs['readonly'] = True
        xii_percentage.widget.attrs['readonly'] = True
        permanent_address.widget.attrs['readonly'] = True
