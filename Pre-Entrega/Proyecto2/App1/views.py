from django.shortcuts import render
from App1.models import Blog, Avatar
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from App1.forms import blogForms
from django.contrib.auth.decorators import login_required

def inicio1(request):
    return render(request, 'App1/in.html')

def about(request):
    return render(request, 'App1/about.html')
def miPerfil(request):
    return render(request, 'App1/miPerfil.html')

def crearBlog(request):
     if request.method == "POST":
        miFormulario = blogForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            blog = Blog(int (informacion['id']), str(informacion['titulo']),str(informacion['subtitulo']),str (informacion['contenido']),str (informacion['autor']))
            blog.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario =blogForms()
             
     return render(request, "App1/crearBlog.html", {"miFormulario": miFormulario})


def leerBlog(request):
    blogs= Blog.objects.all() # trae a todos los profesores
    contexto= {"blogs": blogs}
    return render(request, "App1/leerBlogs.html",contexto)


from django.views.generic import ListView
class blogList(ListView):
    model = Blog
    template_name='/App1/blog_list.html'

from django.views.generic.detail import DetailView
class blogDetalle(DetailView):
    model= Blog
    template_name= "App1/blog_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class blogCreacion(CreateView):
    model=Blog
    success_url="/App1/blog/list"
    fields=['titulo','subtitulo', 'contenido', 'autor']

from django.views.generic.edit import UpdateView
class blogUpdate(UpdateView):
    model= Blog
    success_url= "/App1/blog/list"
    fields=['contenido']

from django.views.generic.edit import DeleteView

class blogDelete( DeleteView,AuthenticationForm):
    def usuario(request):
        usuario = request.user
    model= Blog
    success_url="/App1/blog/list"
    template_name= "App1/blog_confirm-delete.html"

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})

from App1.forms import UserRegisterForm
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
      return render(request,"App1/registro.html" ,  {"form":form})

from App1.forms import blogForms , UserRegisterForm, UserEditForm
# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "App1/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'App1/"inicio".html', {"url":avatares[0].imagen.url})

def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})



@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})

from django.contrib.auth.models import User
from .forms import AvatarFormulario
@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})