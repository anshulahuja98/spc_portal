from django.forms import ModelForm
from .models import JobAdvertisement, InternshipAdvertisement


class JobAdvertisementForm(ModelForm):
    class Meta:
        model = JobAdvertisement
        exclude = ('id',)


class InternshipAdvertisementForm(ModelForm):
    class Meta:
        model = InternshipAdvertisement
        exclude = ('id',)
