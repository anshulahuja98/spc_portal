from django.views.generic import TemplateView
import os
from .models import HomeImageCarousel


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        context['carousel'] = HomeImageCarousel.objects.filter(active=True).order_by('ordering')
        companies = os.listdir("staticfiles/img/company-logo")
        companies = ['img/company-logo/' + image for image in companies]
        context['companies'] = companies
        return context
