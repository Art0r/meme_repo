from rest_framework import serializers
from core.models import Registry, Metadata
from core.serializers.metadata import MetadataSerializer


class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(write_only=True)
    metadata = MetadataSerializer()

    class Meta:
        model = Registry
        fields = ('id', 'file', 'metadata', 'created_at', 'updated_at',)

    def create(self, validated_data):

        Registry.objects.create(
            file=validated_data["file"],
            metadata=Metadata.objects.create(
                author_id=validated_data["metadata_author"],
                name=validated_data["metadata_name"]
            )
        )

        super().create(validated_data)
