from django import forms
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    '''
    Form for search bar of the XListView
    '''
    search = forms.CharField(
                            label=_('Search'),
                            max_length=128,
                            help_text=_('Enter your search keywords here')
                            required=True)
