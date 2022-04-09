from django.db import models

# Create your models here.
# class POST: title, pet_category, description, location, img, user
class Post(models.Model):
    title = models.CharField(max_length=32)
    pet_category = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=64)
    img = models.CharField(max_length=128)
    user = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)