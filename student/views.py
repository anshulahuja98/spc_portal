from django.shortcuts import render
from student import forms
# Create your views here.

def addResume(request):
    form = forms.addResume()
    return render(request, 'student/uploadResume.html', context={'form': form})
