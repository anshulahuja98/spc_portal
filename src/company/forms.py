from django.forms import ModelForm
from .models import JobOffer, InternOffer


class JobOfferForm(ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'


class InternOfferForm(ModelForm):
    class Meta:
        model = InternOffer
        fields = '__all__'
