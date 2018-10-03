from django.shortcuts import render
from rest_framework import generics
from .serializers import snappSerializer
from .models import snapp


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = snapp.objects.all()
    serializer_class = snappSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
