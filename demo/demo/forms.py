from django import forms
from . import models


class RecipeForm(forms.ModelForm):
    '''
    Recipe's form
    '''

    class Meta:
        fields = ['name', 'description']


class ItemForm(forms.ModelForm):
    '''
    Item's form
    '''

    class Meta:
        fields = ['name', 'quantity']
