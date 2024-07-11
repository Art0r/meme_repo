from core.serializers.registry import RegistrySerializer, Registry
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class RegistryViewSet(ModelViewSet):
    queryset = Registry.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ('get', 'put', 'post', 'delete')
    serializer_class = RegistrySerializer
