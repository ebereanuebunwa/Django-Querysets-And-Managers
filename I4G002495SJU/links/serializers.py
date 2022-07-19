from .models import Link
from rest_framework import serializers


# create a serializer for the Link model
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"  # all fields of the Link model