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
        # Query all MortuaryStaff instances
        staff = MortuaryStaff.objects.all()
        
        # Serialize the staff data using MinimalMortuaryStaffSerializer
        serializer = MinimalMortuaryStaffSerializer(staff, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new MortuaryStaff instance.
        """
        # Serialize the incoming data using MortuaryStaffSerializer
        serializer = MortuaryStaffSerializer(data=request.data)
        
        # Validate and save the serialized data
        if serializer.is_valid():
            serializer.save()
            # Return the serialized data and HTTP 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return validation errors with HTTP 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_staff_count(self, request):
        """
        Handle GET requests to retrieve the count of all MortuaryStaff instances.
        """
        # Count all MortuaryStaff instances
        count = MortuaryStaff.objects.count()
        
        # Return the count in a JSON response
        return Response({'staff_count': count})

# View to handle retrieving, updating MortuaryStaff instances
class MortuaryStaffDetailView(APIView):
    
    def get_object(self, id):
        """
        Retrieve a MortuaryStaff instance by its ID.
        """
        try:
            # Try to get the MortuaryStaff instance by ID
            return MortuaryStaff.objects.get(id=id)
        except MortuaryStaff.DoesNotExist:
            # Raise a NotFound exception if the instance does not exist
            raise NotFound(detail="MortuaryStaff not found.")

    def get(self, request, id):
        """
        Handle GET requests to retrieve a single MortuaryStaff instance.
        """
        # Retrieve the MortuaryStaff instance using the provided ID
        staff = self.get_object(id)
        
        # Serialize the staff data
        serializer = MortuaryStaffSerializer(staff)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing MortuaryStaff instance.
        """
        # Retrieve the MortuaryStaff instance using the provided ID
        staff = self.get_object(id)
        
        # Serialize the updated data using MortuaryStaffSerializer
        serializer = MortuaryStaffSerializer(staff, data=request.data)
        
        # Validate and save the updated data
        if serializer.is_valid():
            serializer.save()
            # Return the serialized data and HTTP 200 OK status
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Return validation errors with HTTP 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
