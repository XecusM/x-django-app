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
    search_fields = list()
    filter_fields = list()
    model = object()
    queryset = object()
    order_by = list()
    success_url = str()

    def post(self, request, *args, **kwargs):
        '''
        add keywords to url in post search
        '''
        keys =list()
        if request.POST['search']:
            keys.append(f"search={request.POST['search']}")

        return get_success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        '''
        Get the context for this view.
        '''
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('filter'):
            filter = self.request.GET.get('filter')
            kwargs.update({'filter': filter})
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
        get articles
        '''
        if self.queryset:
            queryset = self.queryset
        else:
            queryset = self.model.objects.all()

        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            queryset = queryset.filter(
                            title__contains=search).order_by('-created_at')
        if self.request.GET.get('filter'):
            filter = self.request.GET.get('filter')
            queryset = queryset.filter(
                            category=filter).order_by('-created_at')
        if self.request.GET.get('sort'):
            sort = self.request.GET.get('sort')
            queryset = queryset.all().order_by(sort)
        
        return queryset
