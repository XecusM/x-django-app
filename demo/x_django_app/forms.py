from django import forms
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    '''
    Form for search bar of the XListView
    '''
    search = forms.CharField(
                            label=_('Search'),
                            max_length=128,
                            help_text=_('Enter your search keywords here'),
                            required=True)

    def __init__(self, *args, **kwargs):
        '''
        Method for initial values and functions for the SearchForm form class
        '''
        try:
            self.fields['search'].initial = kwargs.pop('search')
        except Exception:
            pass

        # get the initial form class values
        super(SearchForm, self).__init__(*args, **kwargs)
