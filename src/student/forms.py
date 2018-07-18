from django.forms import ModelForm
from company.models import JobOffer, InternshipOffer


class JobOfferForm(ModelForm):
    class Meta:
        model = JobOffer
        fields = ('profile', 'student')


class InternshipOfferForm(ModelForm):
    class Meta:
        model = InternshipOffer
        fields = ('profile', 'student',)
