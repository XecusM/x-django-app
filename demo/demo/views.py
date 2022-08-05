from . import models
from x_django_app.views import XListView


class Index(XListView):
    '''
    Index page for recipes and items
    '''
    template_name = 'demo/index.html'
    model = models.Recipe
    search_fields = ['name', 'description']
    queryset = models.Recipe.objects.all()
    ordering = ('name', 'description')
    paginate_by = 20
