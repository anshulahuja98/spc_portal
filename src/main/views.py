from django.views.generic import TemplateView
from .models import PastRecruiters, CoreTeamContacts, Volunteers, News, AlumniTestimonial, HomeImageCarousel


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        context['carousel'] = HomeImageCarousel.objects.filter(active=True).order_by('ordering')
        context['news_list'] = News.objects.filter(active=True).order_by('order_no')
        context['companies'] = PastRecruiters.objects.filter(active=True).order_by('company_order_no')
        context['contacts'] = CoreTeamContacts.objects.filter(active=True).order_by('order_no')
        context['volunteers'] = Volunteers.objects.filter(active=True).order_by('order_no')
        context['testimonial_list'] = AlumniTestimonial.objects.filter(active='True').order_by('ranking')
        return context
