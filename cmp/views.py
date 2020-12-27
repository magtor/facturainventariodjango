from django.shortcuts import render
from django.views import generic
from django.urls import  reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models  import Proveedor
from  cmp.forms import ProveedorForm
from django.http import  HttpResponse
import json

class ProveedorView(LoginRequiredMixin,generic.ListView):
      model =  Proveedor
      template_name = 'cmp/proveedor_list.html'
      context_object_name = 'obj' 
      login_url = 'bases:login'

class ProveedorNew(LoginRequiredMixin,generic.CreateView):
      model = Proveedor
      template_name = 'cmp/proveedor_form.html'
      context_name_object  = 'obj'
      form_class =  ProveedorForm
      success_url = reverse_lazy("cmp:proveedor_list")
      login_url = "bases:login" 
      
      def form_valid(self, form):
         form.instance.uc =  self.request.user
         return super().form_valid(form)
 

class ProveedorEdit(LoginRequiredMixin,generic.UpdateView):
      model = Proveedor
      template_name = "cmp/proveedor_form.html" 
      context_object_name = 'obj'
      form_class = ProveedorForm
      success_url = reverse_lazy("cmp:proveedor_list")
      login_url = "bases:login"

      def form_valid(self, form):
          form.instance.um =  self.request.user.id
          return super().form_valid(form) 

def proveedor_inactivar(request,id):
   template_name = "cmp/inactivar_prv.html" 
   contexto = {}
   proveedor = Proveedor.objects.filter(pk=id).first()
   if not  proveedor:
     return HttpResponse('Proveedor No Existe' + str(id))   

   if request.method=='GET':
      contexto = {'obj':proveedor}
   
   if request.method=='POST':
      proveedor.estado = False
      proveedor.save()
      prv.contexto = {'obj':'ok'}
      return   redirect("cmp:proveedor_list")
      #   return  HttpResponse('Proveedor Inactivado')
      

   return render(request,template_name,contexto)  
  

