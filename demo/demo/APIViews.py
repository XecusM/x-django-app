from . import models
from x_django_app.APIViews import (
                                XCreateAPIView,
                                XRetrieveUpdateAPIView,
                                XDestroyAPIView
)

from . import models, serializers


class RecipeCreateView(XCreateAPIView):
    '''
    Create New Recipe
    '''
    serializer_class = serializers.RecipeSerializer


class RecipeUpdateView(XRetrieveUpdateAPIView):
    '''
    Update Recipe
    '''
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class RecipeDeleteView(XDestroyAPIView):
    '''
    Delete Recipe
    '''
    queryset = models.Recipe.objects.all()