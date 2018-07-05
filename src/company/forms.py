from django.forms import ModelForm
from .models import JobAdvertisement, InternshipAdvertisement


class JobOfferForm(ModelForm):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


class InternOfferForm(ModelForm):
    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'
