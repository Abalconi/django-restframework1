from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

from e_commerce.models import Comic
from e_commerce.api.serializers import ComicSerializer  # Asegúrate de importar tu serializador ComicSerializer

@api_view(['GET'])
def comic_retrieve_api_view(request, id):
    instance = get_object_or_404(Comic, id=id)
    serializer = ComicSerializer(instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def comic_list_api_view(request):
    queryset = Comic.objects.all()
    serializer = ComicSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@parser_classes([JSONParser])
def comic_create_api_view(request):
    serializer = ComicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
