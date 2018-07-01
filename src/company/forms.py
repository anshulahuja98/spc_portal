from django.forms import ModelForm
from .models import JobAdvertisement, InternAdvertisement


class JobOfferForm(ModelForm):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


class InternOfferForm(ModelForm):
    class Meta:
        model = InternAdvertisement
        fields = '__all__'
