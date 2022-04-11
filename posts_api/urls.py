from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'), # api/contacts will be routed to the ContactList view for handling
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'), # api/contacts will be routed to the ContactDetail view for handling
]