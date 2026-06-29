from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path ("", views.tarefasView, name="home"),
    path("adicionar/", views.adicionarTarefa, name="adicionar"),
    path("remover/<int:id>", views.removerTarefa, name="remover"),
    path("editar/<int:id>", views.editarTarefa, name="editar")
]