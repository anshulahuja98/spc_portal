from django.views.generic import TemplateView
import os
from .models import HomeImageCarousel


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        carousel = os.listdir("media")
        print(carousel)
        carousel.sort(key=lambda x: os.path.getmtime('media/' + x), reverse=True)
        print(carousel)
        carousel = ['/' + image for image in carousel]
        context['carousel'] = carousel
        context['carousel'] = HomeImageCarousel.objects.filter(active=True).order_by('image_no')
        companies = os.listdir("staticfiles/img/company-logo")
        companies = ['img/company-logo/' + image for image in companies]
        context['companies'] = companies
        return context
        