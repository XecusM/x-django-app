from django import forms
from . import models


class RecipeForm(forms.ModelForm):
    '''
    Recipe's form
    '''

    class Meta:
        model = models.Recipe
        fields = ['name', 'description']


class ItemForm(forms.ModelForm):
    '''
    Item's form
    '''

    class Meta:
        model = models.Item
        fields = ['recipe', 'name', 'quantity']
