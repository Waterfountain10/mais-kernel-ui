from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def upload_document(request):
    context = {'pdf_url': None}

    if request.method == "POST" and request.FILES.get("pdf_document"):
        pdf_file = request.FILES["pdf_document"]
        file_name = default_storage.save(f"{pdf_file.name}", ContentFile(pdf_file.read()))
        file_url = default_storage.url(file_name)
        context['pdf_url'] = file_url

        pdf_file.seek(0)
    else:
        return JsonResponse({"error": "Document could not be uploaded correctly..."})
