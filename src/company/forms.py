from django.forms import ModelForm
from .models import JobProfile, InternshipProfile


class JobOfferForm(ModelForm):
    class Meta:
        model = JobProfile
        fields = '__all__'


class InternOfferForm(ModelForm):
    class Meta:
        model = InternshipProfile
        fields = '__all__'
