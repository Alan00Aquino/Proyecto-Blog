from django.shortcuts import render
from .models import Post
from .forms import CrearPostForm
from django.urls import reverse

# Para trabajar con vistas basadas en Clases
from django.views.generic import ListView, DetailView, CreateView

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

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('-publicado')
        return consulta_ordenada


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()

class Postear(CreateView):
    model = Post
    template_name = 'posts/postear.html'
    form_class = CrearPostForm

    """
    def get_success_url(self):
        return reverse('posts:posts')
    """