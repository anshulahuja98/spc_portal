from django import forms
from accounts import models


class addResume(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields='__all__'
        exclude =('verified',)
