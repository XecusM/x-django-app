from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
                                TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView
                            )
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.db import transaction

from . import models, forms
from x_django_app.views import XListView


class Index(XListView):
    '''
    Index page for recipes and items
    '''
    template_name = 'demo/index.html'
    model = models.Recipe
    search_fields = ['name', 'description']
