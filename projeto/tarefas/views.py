from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest 
from .forms import TarefaForm
from .models import TarefaModel

def tarefasView(request):
    contexto = {
        "nome": "Leonardo",
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, "tarefas.html", contexto)

def adicionarTarefa(request: HttpRequest):
    if(request.method == "POST"):
        formulario = TarefaForm(request.POST)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("tarefas:home")
    contexto = {
        "form": TarefaForm
    }
    return render(request, "adicionarTarefa.html", contexto)

def removerTarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def editarTarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if(request.method == "POST"):
        formulario = TarefaForm(request.POST, instance = tarefa)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("tarefas:home")
    
    formulario = TarefaForm(instance=tarefa)
    contexto = {
        "form": formulario
    }
    return render(request, "editarTarefa.html", contexto)