from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from App1.forms import *
from users.forms import UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required
from users.models import Avatar

#Inicio de Sesion
def login_request(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "App1/inicio.html", {"name": usuario ,"mensaje":f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "users/login.html", {"mensaje":"Datos incorrectos", 'form': form })
           
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

#Registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"users/register.html" ,  {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            if informacion['password1'] != informacion['password2']:
                datos ={
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial= datos)
            else:
                usuario.email = informacion['email']
                if informacion['password1']: 
                    usuario.set_password = informacion['password1']
                usuario.first_name = informacion['first_name']
                usuario.last_name = informacion['last_name']

                usuario.save()
                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=informacion['imagen'])
                    avatar.save()
                else:   
                   avatar.imagen = informacion["imagen"]
                   avatar.save()

                return render(request, "App1/inicio.html")

    else:
        datos ={
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "users/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})
