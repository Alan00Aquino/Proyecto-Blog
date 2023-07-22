from django.urls import path,include
from .views import posts
from apps.usuarios import views

urlpatterns = [
    path('posts/', posts, name = 'posts'),
]
