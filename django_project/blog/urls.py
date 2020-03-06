from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCrateView,
                    PostUpadteView,
                    PostDeleteView,
                    UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCrateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpadteView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
    
] 


#<app>/<model>_<viewtype>.html