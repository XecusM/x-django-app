from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from demo import models

import os

index_url = reverse('index')


class DemoViewsTests(TestCase):
    '''
    Test all demo application root
    '''

    def test_index_get(self):
        '''
        Test get index page
        '''
        models.Recipe.objects.create(
                                    name='New Recipe 1',
                                    description='Just a new recipe 1')
        models.Recipe.objects.create(
                                    name='New Recipe 2',
                                    description='Just a new recipe 2')

        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'demo/index.html')

        got_recipes = response.context['recipe_list']

        self.assertEqual(len(got_recipes), 2)
