from django.test import TestCase

from demo import forms, models


class DemoFormsTests(TestCase):
    '''
    Test all forms in demo application
    '''
    def setUp(self):
        '''
        Iniital method for all tests
        '''
        self.recipe = models.Recipe.objects.create(
                                            name='New Recipe',
                                            description='Just a new recipe')
        self.item = models.Item.objects.create(
                                            recipe=self.recipe,
                                            name='New Item',
                                            quantity=5)

    def test_recipe_form_fields(self):
        '''
        Test recipe form fields
        '''
        expected = ['name', 'description']

        actual = list(forms.RecipeForm().fields)

        self.assertSequenceEqual(expected, actual)

    def test_recipe_form_valid_data(self):
        '''
        Test recipe form with valid data
        '''
        payload = {'name': 'Another Recipe', 'description': "Let's Rock"}

        form = forms.RecipeForm(data=payload)

        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid_data(self):
        '''
        Test recipe form with invalid data
        '''
        form_name = forms.RecipeForm(
                                    data={
                                        'name': '',
                                        'description': "Let's Rock",
                                    })

        self.assertFalse(form_name.is_valid())

        form_description = forms.RecipeForm(
                                    data={
                                        'name': 'Another Recipe',
                                        'description': '',
                                    })

        self.assertFalse(form_description.is_valid())

    def test_item_form_fields(self):
        '''
        Test item form fields
        '''
        expected = ['recipe', 'name', 'quantity']

        actual = list(forms.ItemForm().fields)

        self.assertSequenceEqual(expected, actual)

    def test_item_form_valid_data(self):
        '''
        Test item form with valid data
        '''
        payload = {
                    'recipe': self.recipe.id,
                    'name': 'Another Item',
                    'quantity': 5
            }

        form = forms.ItemForm(data=payload)

        self.assertTrue(form.is_valid())

    def test_item_form_invalid_data(self):
        '''
        Test item form with invalid data
        '''
        form_name = forms.ItemForm(
                                    data={
                                        'recipe': self.recipe.id,
                                        'name': '',
                                        'quantity': 5,
                                    })

        self.assertFalse(form_name.is_valid())

        form_description = forms.ItemForm(
                                    data={
                                        'recipe': self.recipe.id,
                                        'name': 'Another Item',
                                        'quantity': '',
                                    })

        self.assertFalse(form_description.is_valid())
