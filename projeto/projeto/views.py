from django.http import HttpResponse
from django.shortcuts import render

def testeView(request):
    return HttpResponse("Essa é a rota de teste")

def indexView(request):
    return render(request, "index.html")
