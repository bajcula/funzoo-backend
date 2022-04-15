from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'), # api/contacts will be routed to the ContactList view for handling
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('user/<int:id>/', views.UsersPostsList.as_view(), name='users_posts_list'),
    path('<int:postID>/<int:usersID>/save', csrf_exempt(views.LikeView), name='like_post'),
    path('<int:postID>/<int:usersID>/unsave', csrf_exempt(views.UnlikeView), name='unlike_post')
]