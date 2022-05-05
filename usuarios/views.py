from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import CustomUsuario

class IndexView(ListView):
    models = CustomUsuario
    template_name = 'index.html'
    queryset = CustomUsuario.objects.all()
    context_object_name = 'pessoas'

class CreateUsuarioView(CreateView):
    model = CustomUsuario
    template_name = 'usuario_form.html'
    fields = ['first_name','last_name','email', 'fone','pais', 'estado', 'municipio', 'cep', 'rua', 'numero', 'complemento', 'pis']
    success_url = reverse_lazy('index')

class UpdateUsuarioView(UpdateView):
    model = CustomUsuario
    template_name = 'usuario_form.html'
    fields = ['first_name','last_name','email', 'fone', 'pais', 'estado', 'municipio', 'cep', 'rua', 'numero', 'complemento', 'pis']
    success_url = reverse_lazy('index')

class DeleteUsuarioView(DeleteView):
    model = CustomUsuario
    template_name = 'usuario_del.html'
    success_url = reverse_lazy('index')
