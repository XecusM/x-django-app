from django.shortcuts import render
from django.views.generic import (
                                TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView
                            )
# Create your views here.


class XListView(ListView):
    '''
    List view with search and sort criteria
    '''
