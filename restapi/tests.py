from django.test import TestCase
from .models import snapp
# Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class SnappTestCase(TestCase):
    """This class defines the test suite for the snapp model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.snapp_name = "This is first test api"
        self.snapp_name = snapp(name=self.snapp_name)

    def test_model_can_create_a_snapp(self):
        """Test the snapp model can create a snapp."""
        old_count = snapp.objects.count()
        self.snapp.save()
        new_count = snapp.objects.count()
        self.assertNotEqual(old_count, new_count)

# Create your tests here.


# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.snapp_data = {'name': 'Go to snapp'}
        self.response = self.client.post(
            reverse('create'),
            self.snapp_data,
            format="json")

    def test_api_can_create_a_snapp(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)