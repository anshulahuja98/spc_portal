from django import forms

from .models import Resume


class ResumeForm(forms.Form):
    class Meta:
        model = Resume
        fields = ('file',)
