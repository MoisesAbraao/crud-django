from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome']

    def form_valid(self, form):
        cliente = form.save(commit=False)
        nome = cliente.nome
        cliente.save()
        return redirect('clientes_lista')

class ClientesList(ListView):
    model = Cliente
    fields = ['nome']

class ClientesUpdate(UpdateView):
    model = Cliente
    fields = ['nome']

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes_lista')