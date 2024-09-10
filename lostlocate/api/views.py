from django.shortcuts import render
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomUserSerializer


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
