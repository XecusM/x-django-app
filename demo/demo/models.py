from django.db import models
from django.utils.translation import ugettext_lazy as _

from x_django_app.models import XModel


class Recipe(models.Model, XModel):
    '''
    Model for Recipes
    '''
    name = models.CharField(
                        verbose_name=_('Name'),
                        max_length=128,
                        unique=True,
                        blank=False,
                        null=False
    )
    description = models.CharField(
                        verbose_name=_('Description'),
                        max_length=255,
                        blank=False,
                        null=False
    )
    created_at = models.DateTimeField(
                        verbose_name=_('Created at'),
                        auto_now_add=True,
                        blank=False
    )

    def __str__(self):
        '''
        String representation
        '''
        return self.name


class Item(models.Model, XModel):
    '''
    Model for recipe's items
    '''
    recipe = models.ForeignKey(
                        'Recipe',
                        verbose_name=_('Recipe'),
                        related_name='item_recipe',
                        on_delete=models.CASCADE,
                        blank=True,
                        null=True
    )
    name = models.CharField(
                        verbose_name=_('Name'),
                        max_length=128,
                        unique=False,
                        blank=False,
                        null=False
    )
    quantity = models.IntegerField(
                        verbose_name=_('Quantity'),
                        unique=False,
                        blank=False,
                        null=False
    )
    created_at = models.DateTimeField(
                        verbose_name=_('Created at'),
                        auto_now_add=True,
                        blank=False
    )


    def __str__(self):
        '''
        String representation
        '''
        return f"{self.recipe.name}-{self.name}"
