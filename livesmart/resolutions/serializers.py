from rest_framework import serializers
from resolutions.models import Resolution


class ResolutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resolution
        fields = ('id', 'title', 'body')
