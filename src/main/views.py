from django.views.generic import TemplateView,ListView
import os
from .models import nEws
from django.shortcuts import render

class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        carousel = os.listdir("staticfiles/img/homepage-carousel")
        print(carousel)
        carousel.sort(key=lambda x: os.path.getmtime('staticfiles/img/homepage-carousel/' + x), reverse=True)
        print(carousel)
        carousel = ['img/homepage-carousel/' + image for image in carousel]
        context['carousel'] = carousel
        companies = os.listdir("staticfiles/img/company-logo")
        companies = ['img/company-logo/' + image for image in companies]
        context['companies'] = companies
        context['objt']= nEws.objects.filter(do_show=True).order_by('order_no')
        return context

'''def home(request):
    obj = nEws.objects.all()
    return render(request,"templates/main/index.html", {'objt':obj} )'''

