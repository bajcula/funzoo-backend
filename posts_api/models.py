from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# class POST: title, pet_category, description, location, img, user
class Post(models.Model):
    title = models.CharField(max_length=32)
    pet_category = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=64)
    img = models.CharField(max_length=256)
    authorID = models.ForeignKey(User, on_delete=models.CASCADE)
    authorName = models.CharField(max_length=64, default='anonymus user')
    created_at = models.DateTimeField(auto_now_add=True)