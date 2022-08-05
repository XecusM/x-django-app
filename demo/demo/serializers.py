#data serializers.py
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from . import models


class RecipeSerializer(serializers.ModelSerializer):
    '''
    Serializer for recipes
    '''
    class Meta:
        model = models.Recipe
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ('id', 'created_at')


class ItemSerializer(serializers.ModelSerializer):
    '''
    Serializer for items
    '''
    class Meta:
        model = models.Item
        fields = ['id', 'recipe', 'name', 'quantity', 'created_at']
        read_only_fields = ('id', 'created_at')