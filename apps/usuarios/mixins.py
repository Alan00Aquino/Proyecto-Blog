from django.contrib.auth.mixins import UserPassesTestMixin

class SuperusuarioPostMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()

        return usuario == obj.creador or usuario.is_superuser


class SuperusuarioComentarioMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()

        return usuario == obj.autor or usuario.is_superuser or usuario == obj.posts.creador

class EsColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.es_colaborador or user.is_superuser
    

class MiembroMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Usuario Registrado').exists() or self.request.user.is_superuser