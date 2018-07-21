from django.views.generic import TemplateView
import os


class HomepageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        carousel = os.listdir("staticfiles/img/homepage-carousel")
        carousel = ['img/homepage-carousel/' + image for image in carousel]
        context['carousel'] = carousel
        return context
