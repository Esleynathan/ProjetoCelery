from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image, ImageDraw
import os
from hashlib import sha256

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):
    
    def cria_convite(nome, email):
        template = os.path.join(settings.STATIC_ROOT,'img/convite.png')
        img = Image.open(template)
        img_escrever = ImageDraw.Draw(img)
        img_escrever.text((210,450), nome, fill=(200, 89, 255))
        chave_secreta = "JjHGFD@##Y6#58h&GFJG"
        email = email + chave_secreta
        token = sha256(email.encode()).hexdigest()
        path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
        img.save(path_salvar)

        return token
    
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    
    token = cria_convite(nome, email)
                 
    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()

    send_mail('Cadastro Confirmado.', 'Seu cadastro concluido com sucesso.', 'esleynathan@hotmail.com', recipient_list=[email])
    return render(request,'cadastro_confirmado.html',{'token': token})