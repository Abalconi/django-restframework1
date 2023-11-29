from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.views import APIView

from e_commerce.models import Comic
from e_commerce.api.serializers import ComicSerializer  # Asegúrate de importar tu serializador ComicSerializer

# Reemplaza las funciones de vistas con las clases de DRF

class ComicListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        _queryset = Comic.objects.filter(precio__gte=5.00)
        _serializer = ComicSerializer(_queryset, many=True)
        return Response(data=_serializer.data, status=status.HTTP_200_OK)

class ComicRetrieveAPIView(APIView):
    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Comic, id=request.query_params.get('id'))
        _serializer = ComicSerializer(instance)
        return Response(data=_serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
class ComicCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        _marvel_id = request.data.get('marvel_id')
        if not _marvel_id:
            raise ValidationError({"marvel_id": "Este campo no puede ser nulo."})
        
        _instance, _created = Comic.objects.get_or_create(marvel_id=_marvel_id, defaults=request.data)
        
        if _created:
            _serializer = ComicSerializer(_instance)
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={"marvel_id": "Ya existe un comic con ese valor, debe ser único."},
                        status=status.HTTP_400_BAD_REQUEST)