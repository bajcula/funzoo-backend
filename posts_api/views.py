from audioop import reverse
from json import JSONEncoder
from tokenize import Number
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from .serializers import PostSerializer
from .models import Post, User
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    
class UsersPostsList(generics.ListCreateAPIView):
    # queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use
    http_method_names = ['get']

    # 2nd TRY
    def get(self, request, **kwargs):
        posts = Post.objects.all()
        filteredPosts = posts.filter(authorID_id=kwargs["id"])
        # print('this isssssss', kwargs['id'])
        # print(filteredPosts.values())
        data = list(filteredPosts.values())
        return JsonResponse(data, safe=False)   
        
     
def LikeView(request, postID, usersID):
    post = Post.objects.get(id=postID)
    post.users_liked_by.add(usersID)
    # post.popularity += 1
    return HttpResponse(content=post)

def UnlikeView(request, postID, usersID):
    post = Post.objects.get(id=postID)
    # post.popularity -= 1
    post.users_liked_by.remove(usersID)
    return HttpResponse(content=post)