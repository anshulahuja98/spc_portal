from django import forms
from accounts.models import CompanyProfile, StudentProfile as accounts_models
from .models import InternOffer, JobOffer


class StudentProfileCreateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class AddJobOffer(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'


class AddInternOffer(forms.ModelForm):
    class Meta:
        model = InternOffer
        fields = '__all__'
