from django.shortcuts import render
from rest_framework import generics, status
from .models import Document
from .serializers import DocumentSerializer, CreateDocumentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DocumentView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CreateDocumentView(APIView):
    serializer_class = CreateDocumentSerializer

    def post(self, request, format=None):
        pass




