from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image, ImageDraw
import os
from hashlib import sha256

@shared_task
def cria_convite(nome, email):
    template = os.path.join(settings.STATIC_ROOT,'img/convite.png')
    img = Image.open(template)
    img_escrever = ImageDraw.Draw(img)
    img_escrever.text((210,450), nome, fill=(200, 89, 255))
    chave_secreta = "JjHGFD@##Y6#58h&GFJG"    
    token = sha256((email + chave_secreta).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)

    send_mail('Cadastro Confirmado.', 'Seu cadastro concluido com sucesso. \n Aqui está o link do seu convite: http://127.0.0.1:8000/media/convites/{token}.png', 'esleynathan@hotmail.com', recipient_list=[email])
