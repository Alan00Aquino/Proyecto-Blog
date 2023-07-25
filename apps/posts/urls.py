"""
from django.urls import path,include
from .views import posts
from apps.usuarios import views

urlpatterns = [
    path('posts/', posts, name = 'posts'),
]
"""
from django.urls import path
from .views import PostListView, PostDetailView
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name = 'posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name = 'post_individual'),
    path('postear/', views.Postear.as_view(), name = 'postear'),
]