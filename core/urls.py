from rest_framework.routers import DefaultRouter
from core.views import index
from django.urls import path, include


urlpatterns = [
    path("", index, name='index')
]
