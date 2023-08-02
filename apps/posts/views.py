from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario
from .forms import CrearPostForm, ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from apps.usuarios.mixins import SuperusuarioPostMixin, SuperusuarioComentarioMixin, MiembroMixin, ColaboradorMixin



class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('-publicado')
        return consulta_ordenada


class PostDetailView(DetailView, SuperusuarioPostMixin, SuperusuarioComentarioMixin, MiembroMixin):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
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

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('apps.posts:posts')
    
# Vista para actualizar una publicacion ya existente
class EditarPost(SuperusuarioPostMixin, ColaboradorMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/editar-post.html'
    form_class = CrearPostForm # Uso el mismo de crear una publicacion

    def get_success_url(self):
        return reverse('apps.posts:posts')
    
# Vista que elimina un posteo
class EliminarPost(SuperusuarioPostMixin, ColaboradorMixin, LoginRequiredMixin, DeleteView):
    template_name = 'posts/eliminar-post.html' # Es un template intermedio -esta seguro s-n-
    model = Post


    def get_success_url(self):
        return reverse('apps.posts:posts')
    
class EliminarComentario(View, SuperusuarioComentarioMixin, ColaboradorMixin):
    template_name = 'posts/eliminar-Comentario.html'
    model = Comentario

    def post(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        if request.user == comentario.usuario:
            comentario.delete()
            return redirect('apps.posts:post_individual', id=comentario.posts.id)

    def get(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        return redirect('apps.posts:post_individual', id=comentario.posts.id)