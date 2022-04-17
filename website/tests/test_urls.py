from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import index, get_text

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_get_text_url_is_resolved(self):
        url = reverse('get-text')
        self.assertEquals(resolve(url).func, get_text)
