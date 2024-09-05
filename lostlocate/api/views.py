from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mortuary.models import Mortuary, MortuaryStaff
from .serializers import (
    MortuaryStaffSerializer, MinimalMortuaryStaffSerializer,
)

# Create your views here.

class MortuaryStaffListView(APIView):
    def get(self, request):
        staff = MortuaryStaff.objects.all()
        serializer = MinimalMortuaryStaffSerializer(staff, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MortuaryStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MortuaryStaffDetailView(APIView):
    def get(self, request, id):
        staff = MortuaryStaff.objects.get(id=id)
        serializer = MortuaryStaffSerializer(staff)
        return Response(serializer.data)
    def put(self, request, id):
        staff = MortuaryStaff.objects.get(id=id)
        serializer = MortuaryStaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        staff = MortuaryStaff.objects.get(id=id)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)