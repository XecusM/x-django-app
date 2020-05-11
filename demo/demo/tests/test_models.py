from django.test import TestCase

from demo import models


class DemoModelsTests(TestCase):
    '''
    Test all models in demo application
    '''
    def setUp(self):
        '''
        initiate all test
        '''
        self.recipe = models.Recipe.objects.create(
                                            name='New Recipe',
                                            description='Just a new recipe')

    def test_recipe_create(self):
        '''
        Test is recipe created successfully or not
        '''
        self.assertEqual(models.Recipe.objects.all().count(), 1)

    def test_item_create(self):
        '''
        Test is item created successfully or not
        '''
        models.Item.objects.create(
                                recipe=self.recipe,
                                name='New Item',
                                quantity=5)
        self.assertEqual(models.Item.objects.all().count(), 1)
