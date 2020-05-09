from django.shortcuts import render
from django.views.generic import (
                                TemplateView, ListView,
                                CreateView, UpdateView,
                            )
from django.db.models import Q
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
# Create your views here.


class XListView(ListView):
    '''
    List view with search and sort criteria
    '''
    template_name = None
    model = None
    queryset = None
    ordering = None
    search_fields = None
    success_url = None

    def post(self, request, *args, **kwargs):
        '''
        add keywords to url in post search
        '''
        if request.POST['search']:
            keys.append(f"search={request.POST['search']}")
        else:
            raise Http404

    def get_context_data(self, *, object_list=None, **kwargs):
        '''
        Get the context for this view.
        '''
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            kwargs.update({'search': search})
        if self.request.GET.get('sort'):
            sort = self.request.GET.get('sort')
            kwargs.update({'sort': sort})
        context.update(kwargs)

        return context

    def get_queryset(self):
        '''
        get queryset
        '''
        queryset = super().get_queryset()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
        else:
            ordering = ('id', )
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            fields = None
            for field in self.search_fields:
                if fields is None:
                    fields = f"Q ({field}__contains = '{search}')"
                else:
                    fields += f" | Q ({field}__contains = '{search}')"
            exec(f"queryset = queryset.filter({fields}).order_by(*{ordering})")
        if self.request.GET.get('sort'):
            sort = self.request.GET.get('sort')
            queryset = queryset.all().order_by(sort)

        return queryset
