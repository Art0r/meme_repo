from django.http import JsonResponse
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    return JsonResponse({"res": "Hello World"})
