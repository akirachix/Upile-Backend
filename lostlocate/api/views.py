from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from mortuary_staff.models import MortuaryStaff
from .serializers import MortuaryStaffSerializer, MinimalMortuaryStaffSerializer
from users.models import CustomUser
from .serializers import CustomUserSerializer
from unidentified_bodies.models import UnidentifiedBody
from next_of_kin.models import NextOfKin
from .serializers import UnidentifiedBodySerializer
from .serializers import NextOfKinSerializer
import logging  # Importing logging module

"""Set up logging"""
logger = logging.getLogger(__name__)

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




class CustomUserDetailView(APIView):
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)  
            serializer = CustomUserSerializer(user) 
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
            serializer = CustomUserSerializer(user, data=request.data)     
            if serializer.is_valid():
                serializer.save()              
                return Response(serializer.data, status=status.HTTP_200_OK)          
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


# Create your views here.

class NextOfKinListView(APIView):
    def get(self, request):
        """Retrieve a list of next of kin."""
        logger.info("Fetching list of next of kin.")
        next_of_kin = NextOfKin.objects.all()
        total_next_of_kin = NextOfKin.objects.all().count()
        serializer = NextOfKinSerializer(next_of_kin, many=True)
        logger.info("Successfully fetched next of kin data.")
        return Response({
            'total_next_of_kin': total_next_of_kin,
            'next_of_kin': serializer.data
        })

    def post(self, request):
        """Create a new next of kin entry."""
        logger.info("Creating a new next of kin entry.")
        serializer = NextOfKinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Next of kin entry created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Failed to create next of kin entry: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NextOfKinDetailView(APIView):
    def get(self, request, pk):
        """Retrieve a specific next of kin by primary key."""
        logger.info("Fetching next of kin with pk: %s", pk)
        try:
            next_of_kin = NextOfKin.objects.get(pk=pk)
            serializer = NextOfKinSerializer(next_of_kin)
            logger.info("Successfully fetched next of kin data for pk: %s", pk)
            return Response(serializer.data)
        except NextOfKin.DoesNotExist:
            logger.error("Next of kin with pk: %s not found.", pk)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Update a specific next of kin entry."""
        logger.info("Updating next of kin with pk: %s", pk)
        try:
            next_of_kin = NextOfKin.objects.get(pk=pk)
        except NextOfKin.DoesNotExist:
            logger.error("Next of kin with pk: %s not found.", pk)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NextOfKinSerializer(next_of_kin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Next of kin with pk: %s updated successfully.", pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.warning("Failed to update next of kin with pk: %s: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnidentifiedBodyListView(APIView):
    def get(self, request):
        """Retrieve a list of unidentified bodies."""
        logger.info("Fetching list of unidentified bodies.")
        unidentified_bodies = UnidentifiedBody.objects.all()
        total_unidentified_bodies = UnidentifiedBody.objects.all().count()
        serializer = UnidentifiedBodySerializer(unidentified_bodies, many=True)
        logger.info("Successfully fetched unidentified bodies data.")
        return Response({
            'total_next_of_kin': total_unidentified_bodies,
            'next_of_kin': serializer.data
        })

    def post(self, request):
        """Create a new unidentified body entry."""
        logger.info("Creating a new unidentified body entry.")
        serializer = UnidentifiedBodySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Unidentified body entry created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Failed to create unidentified body entry: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnidentifiedBodyDetailView(APIView):
    def get(self, request, id):
        """Retrieve a specific unidentified body by ID."""
        logger.info("Fetching unidentified body with id: %s", id)
        try:
            unidentified_body = UnidentifiedBody.objects.get(id=id)
            serializer = UnidentifiedBodySerializer(unidentified_body)
            logger.info("Successfully fetched unidentified body data for id: %s", id)
            return Response(serializer.data)
        except UnidentifiedBody.DoesNotExist:
            logger.error("Unidentified body with id: %s not found.", id)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, id):
        """Update a specific unidentified body entry."""
        logger.info("Updating unidentified body with id: %s", id)
        try:
            unidentified_body = UnidentifiedBody.objects.get(id=id)
        except UnidentifiedBody.DoesNotExist:
            logger.error("Unidentified body with id: %s not found.", id)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnidentifiedBodySerializer(unidentified_body, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Unidentified body with id: %s updated successfully.", id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.warning("Failed to update unidentified body with id: %s: %s", id, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
