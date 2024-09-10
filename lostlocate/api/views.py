import logging
from django.db.models import Q
from django.shortcuts import get_object_or_404
from missing_persons.models import MissingPerson
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MissingPersonSerializer, MinimalMissingPersonSerializer

"""Set up logging"""
logger = logging.getLogger(__name__)

class MissingPersonListView(APIView):
    
    def get(self, request):
        """Retrieve a list of all missing persons."""
        missing_people = MissingPerson.objects.all()
        """Total number of missing persons"""
        total_missing_persons = MissingPerson.objects.all().count()
        serializer = MinimalMissingPersonSerializer(missing_people, many=True)
        return Response({
            'total_missing_persons': total_missing_persons,
            'missing_persons': serializer.data
        })

    def post(self, request):
        """Create a new missing person record."""
        serializer = MissingPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MissingPersonDetailView(APIView):
    def get(self, request, id=None):
        """Retrieve a specific missing person by ID or search by name."""
        if id:
            """Handle retrieval by ID"""
            try:
                missing_person = get_object_or_404(MissingPerson, id=id)
                serializer = MissingPersonSerializer(missing_person)
                return Response(serializer.data)
            except Exception as e:
                logger.error(f"Error retrieving missing person with ID {id}: {e}")
                return Response({"error": "An error occurred while retrieving the missing person."}, status=status.HTTP_404_NOT_FOUND)
        else:
            """Handle search by name"""
            name = request.query_params.get('name', None)
            if name:
                try:
                    missing_persons = MissingPerson.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
                    serializer = MissingPersonSerializer(missing_persons, many=True)
                    return Response(serializer.data)
                except Exception as e:
                    logger.error(f"Error searching missing persons by name '{name}': {e}")
                    return Response({"error": "An error occurred while searching for missing persons."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"error": "Name query parameter is required for search."}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        """Update a specific missing person record by ID."""
        try:
            missing_person = get_object_or_404(MissingPerson, id=id)
            serializer = MissingPersonSerializer(missing_person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating missing person with ID {id}: {e}")
            return Response({"error": "Failed to update missing person."}, status=status.HTTP_400_BAD_REQUEST)
