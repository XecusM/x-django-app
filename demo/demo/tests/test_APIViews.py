from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from demo import models
from x_django_app.models import XActivity


class DemoAPITest(TestCase):
    '''
    Test all demo api_views
    '''

    def setUp(self):
        '''
        Initiate the users for tests
        '''
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
                            username='xecus',
                            password='testpassword',
                            first_name='Mohamed',
                            last_name='Aboel-fotouh',
                        )

        self.recipe = models.Recipe.objects.create(
                                    name='New Recipe',
                                    description='Just a new recipe')
        self.item = models.Item.objects.create(
                                    recipe=self.recipe,
                                    name='New Item',
                                    quantity=5)
        
        self.RECIPE_CREATE_URL = reverse('recipe-create')
        self.RECIPE_UPDATE_URL = reverse(
                                        'recipe-update',
                                        kwargs={'pk': self.recipe.id})
        self.RECIPE_DELETE_URL = reverse(
                                        'recipe-delete',
                                        kwargs={'pk': self.recipe.id})
    
    def test_post_recipe_create_success(self):
        '''
        Test Create a new recipe
        '''
        self.client.force_authenticate(user=self.user)

        data = {
                'name': 'Another Recipe',
                'description': 'Just Another Reipe'
                }

        response = self.client.post(self.RECIPE_CREATE_URL, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(XActivity.objects.all().count(), 1)
        self.assertEqual(
                        XActivity.objects.all()[0].activity,
                        XActivity.CREATE)
        
        self.assertEqual(
                        XActivity.objects.all()[0].user,
                        self.user)
    
    def test_patch_recipe_update_success(self):
        '''
        Test update existing recipe
        '''
        self.client.force_authenticate(user=self.user)

        data = {
                'name': 'Another Recipe',
                'description': 'Just Another Reipe'
                }

        response = self.client.patch(self.RECIPE_UPDATE_URL, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(XActivity.objects.all().count(), 1)

        self.assertEqual(
                        XActivity.objects.all()[0].activity,
                        XActivity.EDIT)
        
        self.assertEqual(
                        XActivity.objects.all()[0].user,
                        self.user)
    
    def test_delete_recipe_delete_success(self):
        '''
        Test delete existing recipe
        '''
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(self.RECIPE_DELETE_URL)

        self.assertEqual(
                        response.status_code,
                        status.HTTP_204_NO_CONTENT)
        
        self.assertEqual(XActivity.objects.all().count(), 1)

        self.assertEqual(
                        XActivity.objects.all()[0].activity,
                        XActivity.DELETE)
        
        self.assertEqual(
                        XActivity.objects.all()[0].user,
                        self.user)