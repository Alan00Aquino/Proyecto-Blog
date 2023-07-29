from django.urls import path
from .views import PostListView, PostDetailView
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name = 'posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name = 'post_individual'),
    path('postear/', views.Postear.as_view(), name = 'postear'),
    path('editar-post/<int:pk>', views.EditarPost.as_view(), name = 'editar-post'),
    path('eliminar-post/<int:pk>', views.EliminarPost.as_view(), name = 'eliminar-post'),
]