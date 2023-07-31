from django.urls import path
from .views import PostListView, PostDetailView, Postear, EditarPost, EliminarPost

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('postear/', Postear.as_view(), name='postear'),
    path('editar-post/<int:pk>/', EditarPost.as_view(), name='editar-post'),
    path('eliminar-post/<int:pk>/', EliminarPost.as_view(), name='eliminar-post'),
]