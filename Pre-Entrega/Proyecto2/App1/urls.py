from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio1, name="inicio"),
    path('inicio', views.inicio1, name="inicio"),
    path('blog/list',views.blogList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.blogDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.blogCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.blogUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.blogDelete.as_view(),name='Delete'),
    path('login', views.login_request, name="login"),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name = 'logout'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"), 
    path('agregarAvatar', views.agregarAvatar, name="agregarAvatar"), 
    path('crearBlog', views.crearBlog, name="crearBlog"),
    path('about', views.about, name="about"),
    path('miPerfil', views.miPerfil, name="miPerfil"),
    #blog

    ]
