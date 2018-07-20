from django import forms
from company.models import JobOffer, InternshipOffer
from accounts.models import Resume


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
