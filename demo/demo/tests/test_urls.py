from django.test import TestCase
from django.urls import reverse, resolve

from demo import views


class DemoUrlsTest(TestCase):
    '''
    Test all urls in the demo applciations
    '''
    def test_index_resolved(self):
        '''
        Test index url
        '''
        url = reverse('index')

        self.assertEquals(resolve(url).func.view_class, views.Index)
