from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .models import Sentimenttb
from .serializers import SentimentSerializer

# Create your views here.

class HomeAPIView(TemplateView):
    
    def get(self, request):
        template_name = 'home.html'
        return render(request, template_name)



class SentimentAPIView(APIView):

    def post(self, request):
        serializer = SentimentSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()  # Create a new instance
            # Process the instance or perform additional actions
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)