# to translate our models into json 

from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('uploaded_by', 'file', 'upload_date', 
                  'last_modified', 'title', 'description')

class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('file', 'title', 'description')

