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

urlpatterns = [
    path('posts/', PostListView.as_view(), name = 'posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name = 'post_individual.html'),
]