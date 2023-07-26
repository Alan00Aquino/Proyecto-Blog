from .forms import RegistrarseForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse



class RegistroView(CreateView):
    template_name = 'registration/registro.html'
    form_class = RegistrarseForm
    

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. por favor, inicie sesión.' )
        form.seve()
        
        return redirect('usuarios:login')
    
class LoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request,'Inicio de sesión exitoso')

        return reverse('usuarios:login')
    

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Sesión cerrada con exito.')

        return reverse('usuarios:login')