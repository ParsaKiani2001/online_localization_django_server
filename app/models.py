import uuid

from django.db import models

class LanguageModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,serialize=True,editable=False)
    name = models.CharField(max_length=10,null=False,blank=True,serialize=True)
    local = models.CharField(max_length=10,null=False,blank=True,serialize=True)
    show_lang = models.CharField(max_length=30,null=False,blank=True,serialize=True)
    version = models.IntegerField(null=False,blank=True,serialize=True)
    show_language_icon = models.BinaryField(null=True,blank=True,serialize=True,default=None)
    is_active = models.BooleanField(default=True,blank=True,serialize=True)
    created = models.DateTimeField(auto_now_add=True,serialize=True)

class DictionaryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=True, editable=False)
    keys = models.CharField(max_length=100, null=False, serialize=True, blank=False)
    values = models.TextField(max_length=400, null=False, serialize=True, blank=False)
    local = models.ForeignKey(LanguageModel, on_delete=models.CASCADE, null=False, serialize=True)
    created = models.DateTimeField(auto_now_add=True, serialize=True)