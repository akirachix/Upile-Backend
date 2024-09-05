from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mortuary.models import Mortuary 
from mortuary_staff.models import MortuaryStaff
from police.models import PoliceOfficer 
from stations.models import PoliceStation
from .serializers import (
    MortuaryStaffSerializer, MinimalMortuaryStaffSerializer,
    MinimalPoliceStationSerializer, PoliceStationSerializer, 
    MortuarySerializer, MinimalMortuarySerializer,
    PoliceOfficerSerializer, MinimalPoliceOfficerSerializer
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
    


class PoliceStationListView(APIView):
    def get(self, request):
        stations = PoliceStation.objects.all()
        serializer = MinimalPoliceStationSerializer(stations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PoliceStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PoliceStationDetailView(APIView):
    def get(self, request, id):
        station = PoliceStation.objects.get(id=id)
        serializer = PoliceStationSerializer(station)
        return Response(serializer.data)
    def put(self, request, id):
        station = PoliceStation.objects.get(id=id)
        serializer = PoliceStationSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class MortuaryListView(APIView):
    def get(self, request):
        mortuaries = Mortuary.objects.all()
        serializer = MinimalMortuarySerializer(mortuaries, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MortuarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MortuaryDetailView(APIView):
    def get(self, request, id):
        mortuary = Mortuary.objects.get(id=id)
        serializer = MortuarySerializer(mortuary)
        return Response(serializer.data)
    def put(self, request, id):
        mortuary = Mortuary.objects.get(id=id)
        serializer = MortuarySerializer(mortuary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class PoliceOfficerListView(APIView):
    def get(self, request):
        officers = PoliceOfficer.objects.all()
        serializer = MinimalPoliceOfficerSerializer(officers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PoliceOfficerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PoliceOfficerDetailView(APIView):
    def get(self, request, id):
        officer = PoliceOfficer.objects.get(id=id)
        serializer = PoliceOfficerSerializer(officer)
        return Response(serializer.data)
    def put(self, request, id):
        officer = PoliceOfficer.objects.get(id=id)
        serializer = PoliceOfficerSerializer(officer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    