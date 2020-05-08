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
