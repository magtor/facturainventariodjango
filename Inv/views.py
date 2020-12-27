from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto
from .forms import CategoriaForm,SubCategoriaForm,MarcaForm,UnidadMedidaForm,ProductoForm
# Create your views here.

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model= Categoria
    template_name = "Inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url = reverse_lazy("Inv:categoria_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.uc = self.request.user  
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model= Categoria
    template_name = "Inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url = reverse_lazy("Inv:categoria_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model= Categoria
    template_name = "Inv/catalogos_del.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url = reverse_lazy("Inv:categoria_list")
    
 
class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model= SubCategoria
    template_name = "Inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url = reverse_lazy("Inv:subcategoria_list")
    login_url = "bases:login"
  
    def form_valid(self,form):
        form.instance.uc = self.request.user 
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model= SubCategoria
    template_name = "Inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url = reverse_lazy("Inv:subcategoria_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "Inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model= Marca
    template_name = "Inv/marca_form.html"
    context_object_name = "obj"
    form_class= MarcaForm
    success_url = reverse_lazy("Inv:marca_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.uc = self.request.user  
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model= Marca
    template_name = "Inv/marca_form.html"
    context_object_name = "obj"
    form_class= MarcaForm
    success_url = reverse_lazy("Inv:marca_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)

def marca_inactivar(request,id):
   marca = Marca.objects.filter(pk=id).first()
   contexto = {}
   template_name = "Inv/catalogos_del.html" 
   if not  marca:
     return  redirect("Inv:marca_list")    

   if request.method=='GET':
      contexto = {'obj':marca}
   
   if request.method=='POST':
      marca.estado = False
      marca.save()
      return  redirect("Inv:marca_list")  

   return render(request,template_name,contexto)

class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "Inv/UnidadMedida_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class UMNew(LoginRequiredMixin, generic.CreateView):
    model= UnidadMedida
    template_name = "Inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class= UnidadMedidaForm
    success_url = reverse_lazy("Inv:unidadmedida_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.uc = self.request.user  
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model= UnidadMedida
    template_name = "Inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class= UnidadMedidaForm
    success_url = reverse_lazy("Inv:unidadmedida_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "Inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model= Producto
    template_name = "Inv/producto_form.html"
    context_object_name = "obj"
    form_class= ProductoForm
    success_url = reverse_lazy("Inv:producto_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.uc = self.request.user  
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model= Producto
    template_name = "Inv/producto_form.html"
    context_object_name = "obj"
    form_class= ProductoForm
    success_url = reverse_lazy("Inv:producto_list")
    login_url = "bases:login"
     
    def form_valid(self,form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)

def producto_inactivar(request,id):
   producto = Producto.objects.filter(pk=id).first()
   contexto = {}
   template_name = "Inv/catalogos_del.html" 
   if not  producto:
     return  redirect("Inv:producto_list")    

   if request.method=='GET':
      contexto = {'obj':producto}
   
   if request.method=='POST':
      producto.estado = False
      producto.save()
      return  redirect("Inv:producto_list")  

   return render(request,template_name,contexto)
