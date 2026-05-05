from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("alfajor/", views.alfajor, name="alfajor"),

    path("alfajor/listar/", views.alfajor_listar, name="alfajor_listar"),
    path("alfajor/crear/", views.alfajor_crear, name="alfajor_crear"),
    path("alfajor/editar/<int:id>/", views.alfajor_editar, name="alfajor_editar"),
    path("alfajor/eliminar/<int:id>/", views.alfajor_eliminar, name="alfajor_eliminar"),
]