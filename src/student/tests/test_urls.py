from django.test import SimpleTestCase
from django.urls import reverse, resolve
from student.views import DetailsView, ResumeView, InternshipOffersView, JobOffersView
from accounts.views import StudentRegisterFormView


class TestStudentUrlsResolve(SimpleTestCase):

    def test_details_url_resolves(self):
        url = reverse('student:detail')
        self.assertEquals(resolve(url).func.view_class, DetailsView)

    def test_intern_offers_url_resolves(self):
        url = reverse('student:intern-offers')
        self.assertEquals(resolve(url).func.view_class, InternshipOffersView)

    def test_job_offers_url_resolves(self):
        url = reverse('student:job-offers')
        self.assertEquals(resolve(url).func.view_class, JobOffersView)

    def test_resume_upload_url_resolves(self):
        url = reverse('student:resume_upload')
        self.assertEquals(resolve(url).func.view_class, ResumeView)

    def test_register_url_resolves(self):
        url = reverse('student:register')
        self.assertEquals(resolve(url).func.view_class, StudentRegisterFormView)
