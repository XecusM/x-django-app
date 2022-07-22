from rest_framework import (
                            viewsets, mixins, permissions,
                            status, generics
                            )
from rest_framework.response import Response
from rest_framework import status

from .models import XActivity

# Create your views here.


class XCreateAPIView(generics.CreateAPIView):
    """
    Concrete view for creating a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # Store user activity
        activity = XActivity.objects.create_activity(
                                activity_object=self.object,
                                activity=XActivity.CREATE,
                                user=self.request.user,
                                message=self.get_message(self.object)
        )
        activity.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    def get_message(self, object):
        '''
        return activity messsage for the selected object
        '''
        return f"Object-{object.id}"