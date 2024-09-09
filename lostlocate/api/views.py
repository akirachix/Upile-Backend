from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from mortuary_staff.models import MortuaryStaff
from .serializers import MortuaryStaffSerializer, MinimalMortuaryStaffSerializer

# View to handle listing and creating MortuaryStaff instances
class MortuaryStaffListView(APIView):
    
    def get(self, request):
        """
        Handle GET requests to retrieve a list of all MortuaryStaff.
        """
        staff = MortuaryStaff.objects.all()
        serializer = MinimalMortuaryStaffSerializer(staff, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new MortuaryStaff instance.
        """
        serializer = MortuaryStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_staff_count(self, request):
        """
        Handle GET requests to retrieve the count of all MortuaryStaff instances.
        """
        count = MortuaryStaff.objects.count()
        return Response({'staff_count': count})

# View to handle retrieving, updating MortuaryStaff instances
class MortuaryStaffDetailView(APIView):
    
    def get_object(self, id):
        """
        Retrieve a MortuaryStaff instance by its ID.
        """
        try:
            return MortuaryStaff.objects.get(id=id)
        except MortuaryStaff.DoesNotExist:
            raise NotFound(detail="MortuaryStaff not found.")

    def get(self, request, id):
        """
        Handle GET requests to retrieve a single MortuaryStaff instance.
        """
        staff = self.get_object(id)
        serializer = MortuaryStaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing MortuaryStaff instance.
        """
        staff = self.get_object(id)
        serializer = MortuaryStaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
