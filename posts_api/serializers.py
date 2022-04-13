from rest_framework import serializers 
from .models import Post

class PostSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Post # tell django which model to use
        fields = ('id', 'title', 'pet_category', 'description', 'location', 'img', 'authorID', 'authorName', 'created_at') # tell django which fields to include