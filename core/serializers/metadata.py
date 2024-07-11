from rest_framework import serializers
from core.models import Metadata, Account


class MetadataSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field='username')

    class Meta:
        model = Metadata
        fields = ('name', 'author')
