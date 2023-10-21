from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()

    
class CatalogoFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    valor = forms.IntegerField()
    imagen = forms.ImageField(required=False)
    
class ProveedorFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    
