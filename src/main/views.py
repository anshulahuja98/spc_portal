from django.views.generic import TemplateView
import os
from .models import PastRecruiters, CoreTeamContacts, Volunteers, News


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        carousel = os.listdir("staticfiles/img/homepage-carousel")
        carousel.sort(key=lambda x: os.path.getmtime('staticfiles/img/homepage-carousel/' + x), reverse=True)
        carousel = ['img/homepage-carousel/' + image for image in carousel]
        context['carousel'] = carousel
        context['news_list'] = News.objects.filter(active=True).order_by('order_no')
        context['companies'] = PastRecruiters.objects.filter(active=True).order_by('company_order_no')
        context['contacts'] = CoreTeamContacts.objects.filter(active=True).order_by('order_no')
        context['volunteers'] = Volunteers.objects.filter(active=True).order_by('order_no')
        return context
