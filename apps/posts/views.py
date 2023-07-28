from django.shortcuts import render, redirect
from .models import Post, Comentario
from .forms import CrearPostForm, ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

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
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm() 
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class Postear(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/postear.html'
    form_class = CrearPostForm

    def get_success_url(self):
        return reverse('apps.posts:posts')