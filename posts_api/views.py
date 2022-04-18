from audioop import reverse
from json import JSONEncoder
from tokenize import Number
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from .serializers import PostSerializer, EditPostSerializer
from .models import Post, User
from django.http import JsonResponse
from django.http import  HttpResponse
from django.urls import reverse



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = EditPostSerializer
    
class UsersPostsList(generics.ListCreateAPIView):
    # queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use
    http_method_names = ['get']

    # 2nd TRY
    def get(self, request, **kwargs):
        posts = Post.objects.all().order_by('-id')
        filteredPosts = posts.filter(authorID_id=kwargs["id"])
        # print('this isssssss', kwargs['id'])
        # print(filteredPosts.values())
        data = list(filteredPosts.values())
        return JsonResponse(data, safe=False)   
        
class UsersSavedPostsList(generics.ListCreateAPIView):
    # queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use
    http_method_names = ['get']

    # 2nd TRY
    def get(self, request, **kwargs):
        # PostsSavedByUsers = Post.users_liked_by.through
        # posts = Post.objects.all()
        # filteredPosts = posts.filter(authorID_id=kwargs["id"])
        # filteredPosts = posts.filter(authorID_id=kwargs["id"])
        result = Post.objects.all().order_by('-id')
        # result.values('users_liked_by').filter(id=kwargs["id"])
        usersSavedPostsTuples = result.values_list('users_liked_by', 'id')

        usersSavedPostsTuples = list(usersSavedPostsTuples)
        # for res in result.iterator():
        #     print (res.id, res.users_liked_by.through)
        # usersSavedPosts = PostsSavedByUsers.objects.filter(myuser_id=kwargs["id"]).values('myuser')
        # print('posts saved by users', PostsSavedByUsers)
        # print('this user saved posts', usersSavedPosts)
        # posts_in_saved_table = Post.objects.filter(
        #     id__in=usersSavedPosts
        # )
        usersRealList = []
        data = []
        print('list made', usersSavedPostsTuples)
        for item in usersSavedPostsTuples:
            print ('this is ids of users who liked it', item[0], 'and this is the posts id', item[1])
            if item[0] == kwargs["id"]:
                usersRealList.append(Post.objects.get(id=item[1]))
                print('this is the pair', item[0], item[1])
        
        print('final list', usersRealList)
  
        def PostToDictionary(post):
            if post == None:
                return None

            dictionary = {}
            dictionary["id"] = post.id
            dictionary["title"] = post.title
            dictionary["pet_category"] = post.pet_category
            dictionary["description"] = post.description
            dictionary["location"] = post.location
            dictionary["authorName"] = post.authorName
            dictionary["created_at"] = post.created_at
            dictionary["authorID_id"] = post.authorID_id
            dictionary["img"] = str(post.img)
            
            return dictionary
        
        for list_item in usersRealList:
            data.append(PostToDictionary(list_item))
            
        print('this is data', data)
            
        # data = list(posts_in_saved_table.values())
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