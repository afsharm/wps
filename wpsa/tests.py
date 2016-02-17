from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Workplace
from django.core.urlresolvers import reverse

class WorkplaceMethodTests(TestCase):
	def published_recently(self):
		time = timezone.now() + datetime.timedelta(days=30)
		self.assertEqual(1,1)

def create_wp(province, city):
	return Workplace.objects.create(province=province, city=city)

class WorkplaceViewTests(TestCase):
	def test_index_view_with_no_workplaces(self):
		response = self.client.get(reverse('wpsa:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No Workplace is defined")
		self.assertQuerysetEqual(response.context['active_wp'], [])