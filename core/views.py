from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Contato
from django.urls import reverse_lazy


class IndexView(ListView):
    models = Contato
    template_name = 'index.html'
    queryset = Contato.objects.all()
    context_object_name = 'contatos'
    paginate_by = 9
    ordering = 'nome'


class CreateContatoView(CreateView):
    model = Contato
    template_name = 'contato_form.html'
    fields = ['nome', 'email', 'phone', 'endereco']
    success_url = reverse_lazy('index')


class UpdateContatoView(UpdateView):
    model = Contato
    template_name = 'contato_form.html'
    fields = ['nome', 'email', 'phone', 'endereco']
    success_url = reverse_lazy('index')


class DeleteContatoView(DeleteView):
    model = Contato
    template_name = 'contato_del.html'
    success_url = reverse_lazy('index')


class DetailContatoView(DetailView):
    model = Contato
    template_name = 'contato_info.html'
