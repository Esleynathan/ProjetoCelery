from django.shortcuts import render
from django.http import HttpResponse

def inscricao(request):
    return render(request, 'inscricao.html')