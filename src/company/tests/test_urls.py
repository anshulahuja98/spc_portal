from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from company.views import InternshipAdvertisementFormView, JobAdvertisementFormView, InternshipAdvertisementAddedListView, \
    JobAdvertisementsAddedListView, \
    InternshipOfferView, JobOfferView
from django.contrib.auth.models import User
from accounts.views import CompanyRegisterFormView
from company.models import JobAdvertisement, InternshipAdvertisement
from accounts.models import CompanyProfile
from datetime import date


class TestCompanyUrlsResolve(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.test_company = CompanyProfile.objects.create(name='Test', user=self.test_user, domain='Consulting',
                                                          country='Indian', contact=1234567890)

    def test_internship_offer_url_resolves(self):
        internship_offer = InternshipAdvertisement.objects.create(active=True, company=self.test_company, designation=' ', description=' ',
                                                                  tentative_join_date=date(2030, 10, 23), tentative_job_location=' ',
                                                                  ctc='23.5', bond=False, resume_required=False, aptitude_test_required=False,
                                                                  group_discussion_required=False, medical_test_required=False, min_gpa=3.5)
        url = reverse('company:internship-offer', kwargs={'id': internship_offer.id})
        self.assertEquals(resolve(url).func.view_class, InternshipOfferView)

    def test_job_offer_url_resolves(self):
        job_offer = JobAdvertisement.objects.create(active=True, company=self.test_company, designation=' ', description=' ',
                                                    tentative_join_date=date(2030, 10, 23), tentative_job_location=' ',
                                                    ctc='23.5', bond=False, resume_required=False, aptitude_test_required=False,
                                                    group_discussion_required=False, medical_test_required=False, min_gpa=3.5)
        url = reverse('company:job-offer', kwargs={'id': job_offer.id})
        self.assertEquals(resolve(url).func.view_class, JobOfferView)


class TestCompanyUrlsResolve1(SimpleTestCase):

    def test_intern_offers_added_url_resolves(self):
        url = reverse('company:intern-offers-added')
        self.assertEquals(resolve(url).func.view_class, InternshipAdvertisementAddedListView)

    def test_job_offers_added_url_resolves(self):
        url = reverse('company:job-offers-added')
        self.assertEquals(resolve(url).func.view_class, JobAdvertisementsAddedListView)

    def test_job_offer_form_url_resolves(self):
        url = reverse('company:job-offer-form')
        self.assertEquals(resolve(url).func.view_class, JobAdvertisementFormView)

    def test_internship_offer_form_url_resolves(self):
        url = reverse('company:intern-offer-form')
        self.assertEquals(resolve(url).func.view_class, InternshipAdvertisementFormView)

    def test_register_url_resolves(self):
        url = reverse('company:register')
        self.assertEquals(resolve(url).func.view_class, CompanyRegisterFormView)
