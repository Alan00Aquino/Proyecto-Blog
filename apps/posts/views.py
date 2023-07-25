from django.shortcuts import render
from .models import Post

# Para trabajar con vistas basadas en Clases
from django.views.generic import ListView, DetailView

# Create your views here.

# Vistas basadas en funciones
"""
def posts(request):
    contexto = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts.html', contexto)
"""

# Vistas basadas en clases
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()