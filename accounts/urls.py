from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyUserList.as_view(), name='user_list'), # api/contacts will be routed to the ContactList view for handling
    path('<int:pk>/', views.MyUserDetail.as_view(), name='user_detail'), # api/contacts will be routed to the ContactDetail view for handling
]