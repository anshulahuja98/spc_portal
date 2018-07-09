from django.forms import ModelForm
from .models import JobAdvertisement, InternshipAdvertisement


class JobAdvertisementForm(ModelForm):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


class InternshipAdvertisementForm(ModelForm):
    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'
