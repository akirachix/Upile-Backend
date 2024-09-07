from django.shortcuts import render
from missing_persons.models import MissingPerson
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

from .serializers import MissingPersonSerializer,MinimalMissingPersonSerializer


class MissingPersonListView(APIView):
    def get(self, request):
        missing_people = MissingPerson.objects.all()
        serializer = MinimalMissingPersonSerializer(missing_people, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MissingPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MissingPersonDetailView(APIView):
    def get(self, request, id):
        missing_person = MissingPerson.objects.get(id=id)
        serializer = MissingPersonSerializer(missing_person)
        return Response(serializer.data)
    
    def put(self, request, id):
        missing_person = MissingPerson.objects.get(id=id)
        serializer = MissingPersonSerializer(missing_person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
