from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path("<int:id_suplemento>", views.suplemento, name="suplemento"),
    path("agregar_suplemento", views.agregar_suplemento, name="agregar_suplemento"),
    path("<int:id_suplemento>/eliminar_suplemento", views.eliminar_suplemento, name="eliminar_suplemento"),
    path("<int:id_suplemento>/modificar_suplemento", views.modificar_suplemento, name="modificar_suplemento"),

    path("categoria/<int:id_categoria>", views.categoria, name="categoria"),
    path("agregar_categoria", views.agregar_categoria, name="agregar_categoria"),
    path("categoria/<int:id_categoria>/eliminar_categoria", views.eliminar_categoria, name="eliminar_categoria"),
    path("categoria/<int:id_categoria>/modificar_categoria", views.modificar_categoria, name="modificar_categoria"),
    path("suplementos_categoria/<int:id_categoria>", views.suplementos_categoria, name="suplementos_categoria"),

    path("marca/<int:id_marca>", views.marca, name="marca"),
    path("agregar_marca", views.agregar_marca, name="agregar_marca"),
    path("marca/<int:id_marca>/eliminar_marca", views.eliminar_marca, name="eliminar_marca"),
    path("marca/<int:id_marca>/modificar_marca", views.modificar_marca, name="modificar_marca"),
    path("suplementos_marca/<int:id_marca>", views.suplementos_marca, name="suplementos_marca"),
]
