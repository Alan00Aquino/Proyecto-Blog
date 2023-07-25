from django.forms import ModelForm
from .models import Post

class CrearPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'activo', 'categoria', 'imagen'] 