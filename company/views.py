from django.shortcuts import render
from company import forms


# Create your views here.

def addjoboffer(request):
    form = forms.AddJobOffer()
    return render(request, 'company/joboffer.html', context={'form': form})


def addinternoffer(request):
    form = forms.AddInternOffer()
    return render(request, 'company/internoffer.html', context={'form': form})
