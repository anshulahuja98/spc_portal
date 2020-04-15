from django.views.generic import TemplateView, DetailView
from .models import CoreTeamContacts, Volunteers, News, AlumniTestimonial, HomeImageCarousel, NavBarSubOptions, \
    CareerCommittee


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        context['carousel'] = HomeImageCarousel.objects.filter(active=True).order_by('ordering')
        context['news_list'] = News.objects.filter(active=True).order_by('order_no')
        context['testimonial_list'] = AlumniTestimonial.objects.filter(active='True').order_by('ranking')
        return context


class NavBarSubOptionsPageView(DetailView):
    template_name = 'main/navbarsuboptionpage.html'
    model = NavBarSubOptions

    def get_context_data(self, **kwargs):
        context = super(NavBarSubOptionsPageView, self).get_context_data()
        context['contacts'] = CoreTeamContacts.objects.filter(active=True).order_by('order_no')
        context['volunteers'] = Volunteers.objects.filter(active=True).order_by('order_no')
        context['c3members'] = CareerCommittee.objects.filter(active=True).order_by('order_no')
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.use_custom_html:
            self.template_name = self.object.custom_html
        else:
            self.template_name = 'main/navbarsuboptionpage.html'
        return self.render_to_response(context)
