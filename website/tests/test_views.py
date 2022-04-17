from django.test import TestCase, Client
from website.views import index, get_text
from django.urls import reverse

class TestViews(TestCase):

    def test_index_view_status_code(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_get_text_view_status_code_get(self):
        client = Client()
        response = client.get(reverse('get-text'))
        self.assertEquals(response.status_code, 405)

    def test_get_text_view_status_code_post(self):
        client = Client()
        response = client.post(reverse('get-text'))
        self.assertEquals(response.status_code, 200)
