from rest_framework.routers import DefaultRouter
from core.views.registry import RegistryViewSet
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()

router.register('registry', RegistryViewSet)

urlpatterns = ([
    path("", include(router.urls))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) +
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

