from json import JSONEncoder

from rest_framework import generics, serializers
from .serializers import PostSerializer
from .models import Post
from django.http import JsonResponse



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
    # TRYING TO FILTER OUT
    # objects = [
    #     my_object 
    #     for my_object in Post.objects.all() 
    #     if my_object.authorID_id == self.kwargs['parameter']
    # ]
    # queryset = objects
    
    #3rd TRY
    # def get_queryset(self):
    #     if self.request.method == 'GET':
    #         queryset = Post.objects.all()
    #         theID = self.request.GET.get('q', None)
    #         if theID is not None:
    #             queryset = queryset.filter(authorID_id=theID)
    #         return queryset
    
    # 2nd TRY
    def get(self, request, **kwargs):
        posts = Post.objects.all()
        filteredPosts = posts.filter(authorID_id=kwargs["id"])
        # print('this isssssss', kwargs['id'])
        # print(filteredPosts.values())
        data = list(filteredPosts.values())
        return JsonResponse(data, safe=False)   
        

        