from django.urls import path
from .views import index, upload_document

urlpatterns = [
    path('', index),
    path('login', index),
    path('upload_document/', upload_document, name='upload_document'),
    path('table', index)
]
