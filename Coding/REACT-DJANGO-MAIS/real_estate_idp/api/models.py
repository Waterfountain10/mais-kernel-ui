from django.db import models
from django.contrib.auth.models import AbstractUser

# this files should be thicc and the views.py, thin

def is_user_unique():
    # authentifiation to do
    return

# User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    # Add related_name to groups and user_permissions to resolve the conflict
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom",
        related_query_name="user",
    )
    # !!! IMPLEMENT USER AUTHENTIFICATION LATER !!!

# Document/File Model
class Document(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

# OCR Result Model
class OCRResult(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    ocr_text = models.TextField()
    processed_date = models.DateTimeField(auto_now_add=True)

# Tag Model for categorizing documents
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    documents = models.ManyToManyField(Document, related_name='tags')

# Optionally, a model for categorizing documents, if needed
class Category(models.Model):
    name = models.CharField(max_length=100)
    documents = models.ManyToManyField(Document, related_name='categories')

