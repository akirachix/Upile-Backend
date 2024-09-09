from django.shortcuts import render
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomUserSerializer



class CustomUserDetailView(APIView):
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)  # Retrieve the user by ID
            serializer = CustomUserSerializer(user)  # Serialize the user data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)  # Handle user not found   
    def put(self, request, id):
        users = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
def put(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)  
            # Retrieve the user by ID
            serializer = CustomUserSerializer(user, data=request.data)  
            # Serialize the updated data
            if serializer.is_valid():
                serializer.save() 
                # Save the updated user data
                return Response(serializer.data, status=status.HTTP_200_OK)  
            # Return the updated data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        # Handle validation errors
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND) 
        # Handle user not found