from django.shortcuts import render
from App1.forms import *
from App1.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def informacion(request): #vista para informacion
    return render(request,'App1/informacion.html')
 
#Vistas basadas en clases para Catalogo
class CatalogoList(ListView):

      model = Catalogo 
      template_name = "App1/catalogo_list.html"

class CatalogoDetalle(DetailView):

      model = Catalogo
      template_name = "App1/catalogo_detalle.html"

class CatalogoCreacion(LoginRequiredMixin,CreateView):

      model = Catalogo
      template_name = "App1/catalogo_form.html"
      success_url = reverse_lazy("CatalogoList")
      fields = ['marca', 'modelo', 'valor', 'imagen']

class CatalogoUpdate(LoginRequiredMixin,UpdateView):

      model = Catalogo
      template_name = "App1/catalogo_edit.html"
      success_url = reverse_lazy("CatalogoList")
      fields = ['marca', 'modelo', 'valor', 'imagen']
      
class CatalogoDelete(LoginRequiredMixin,DeleteView):

      model = Catalogo
      success_url = reverse_lazy("CatalogoList")
      template_name = "App1/catalogo_confirm_delete.html"
      
#Vistas basadas en clases para Clientes

class ClienteList(ListView):

      model = Cliente 
      template_name = "App1/cliente_list.html"

class ClienteDetalle(DetailView):

      model = Cliente
      template_name = "App1/cliente_detalle.html"

class ClienteCreacion(LoginRequiredMixin,CreateView):

      model = Cliente
      template_name = "App1/cliente_form.html"
      success_url = reverse_lazy("ClienteList")
      fields = ['nombre', 'apellido', 'email', 'edad']

class ClienteUpdate(LoginRequiredMixin,UpdateView):

      model = Cliente
      template_name = "App1/cliente_edit.html"
      success_url = reverse_lazy("ClienteList")
      fields = ['nombre', 'apellido', 'email', 'edad']
      
class ClienteDelete(LoginRequiredMixin,DeleteView):

      model = Cliente
      success_url = reverse_lazy("ClienteList")
      template_name = "App1/cliente_confirm_delete.html" 
      
#Vistas basadas en clases para Proveedores  
      
class ProveedorList(ListView):

      model = Proveedor 
      template_name = "App1/proveedor_list.html"

class ProveedorDetalle(DetailView):

      model = Proveedor
      template_name = "App1/proveedor_detalle.html"

class ProveedorCreacion(LoginRequiredMixin,CreateView):

      model = Proveedor
      template_name = "App1/proveedor_form.html"
      success_url = reverse_lazy("ProveedorList")
      fields = ['nombre', 'direccion', 'email', 'telefono']

class ProveedorUpdate(LoginRequiredMixin,UpdateView):

      model = Proveedor
      template_name = "App1/proveedor_edit.html"
      success_url = reverse_lazy("ProveedorList")
      fields = ['nombre', 'direccion', 'email', 'telefono']
      
class ProveedorDelete(LoginRequiredMixin,DeleteView):

      model = Proveedor
      success_url = reverse_lazy("ProveedorList")
      template_name = "App1/proveedor_confirm_delete.html"              