from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drfapp.serializers import StudentSerializer
from drfapp.models import Student
from rest_framework.permissions import IsAuthenticated



class TestView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    
    
    def get(self, request, *args, **kwargs):
         qs = Student.objects.all()
         student1 = qs.first()
         Serializer = StudentSerializer( student1)
         return Response(Serializer.data)
    
    def post(self, request, *args, **kwargs):
        Serializer = StudentSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        return Response(Serializer.errors)
