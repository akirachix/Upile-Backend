from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mortuary.models import Mortuary
from police.models import PoliceOfficer
from stations.models import PoliceStation
from .serializers import (
    PoliceStationSerializer,
    MortuarySerializer, 
    PoliceOfficerSerializer 
)

# Create your views here.

class PoliceStationListView(APIView):
    def get(self, request):
        """Retrive the police stations"""
        stations = PoliceStation.objects.all()
        serializer =PoliceStationSerializer(stations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PoliceStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PoliceStationDetailView(APIView):
    def get(self, request, id):
        try:
            """Retrieve the PoliceStation object by ID"""
            station = PoliceStation.objects.get(id=id)
            serializer = PoliceStationSerializer(station)
            return Response(serializer.data)
        except PoliceStation.DoesNotExist:
            """Handle the case where the police station with the given ID does not exist"""
            return Response({'error': 'Police station not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            """Retrieve the PoliceStation object by ID for updating"""
            station = PoliceStation.objects.get(id=id)
            serializer = PoliceStationSerializer(station, data=request.data)
            
            """Validate and save the updated police station details if valid"""
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            """ Return validation errors if the data is not valid"""
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PoliceStation.DoesNotExist:
            """Handle the case where the police station with the given ID does not exist"""
            return Response({'error': 'Police station not found'}, status=status.HTTP_404_NOT_FOUND)

    


class MortuaryListView(APIView):
    def get(self, request):
        mortuaries = Mortuary.objects.all()
        serializer = MortuarySerializer(mortuaries, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MortuarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MortuaryDetailView(APIView):
    def get(self, request, id):
        try:
            """Try to retrieve the Mortuary object by ID"""
            mortuary = Mortuary.objects.get(id=id)
            serializer = MortuarySerializer(mortuary)
            return Response(serializer.data)
        except Mortuary.DoesNotExist:
            """Handle the case where the mortuary with the given ID does not exist"""
            return Response({'error': 'Mortuary not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            """Try to retrieve the Mortuary object by ID for updating"""
            mortuary = Mortuary.objects.get(id=id)
            serializer = MortuarySerializer(mortuary, data=request.data)
            
            """Validate and save the updated mortuary details if valid"""
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            """Return validation errors if the data is not valid"""
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mortuary.DoesNotExist:
            """Handle the case where the mortuary with the given ID does not exist"""
            return Response({'error': 'Mortuary not found'}, status=status.HTTP_404_NOT_FOUND)

    


class PoliceOfficerListView(APIView):
    def get(self, request):
        total_police_officers = PoliceOfficer.objects.all().count()
        officers = PoliceOfficer.objects.all()
        serializer = PoliceOfficerSerializer(officers, many=True)
        return Response({
            'total_police_officers': total_police_officers,
            'officers': serializer.data
        })
    def post(self, request):
        serializer = PoliceOfficerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
class PoliceOfficerDetailView(APIView):
    def get(self, request, id):
        try:
            """Try to retrieve the PoliceOfficer object by ID"""
            officer = PoliceOfficer.objects.get(id=id)
            serializer = PoliceOfficerSerializer(officer)
            return Response(serializer.data)
        except PoliceOfficer.DoesNotExist:
            """Handle the case where the police officer with the given ID does not exist"""
            return Response({'error': 'Police officer not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            """Try to retrieve the PoliceOfficer object by ID for updating"""
            officer = PoliceOfficer.objects.get(id=id)
            serializer = PoliceOfficerSerializer(officer, data=request.data)
            
            """Validate and save the updated police officer details if valid"""
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            """Return validation errors if the data is not valid"""
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PoliceOfficer.DoesNotExist:
            """Handle the case where the police officer with the given ID does not exist"""
            return Response({'error': 'Police officer not found'}, status=status.HTTP_404_NOT_FOUND)
