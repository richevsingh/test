from rest_framework import serializers
from .models import snapp


class snappSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = snapp
        fields = ('userid', 'paragraph', 'label', 'textbox', 'timestamp')
        read_only_fields = ('timestamp')