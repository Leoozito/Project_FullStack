from django.db import models
import string
import random

def gerar_unique_code():
    length = 6 # mandar o código com 6 de tamanho para o max de 8
    
    while True: # enquanto for True, gera código e retorna código
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # gerando código aleatórios por aq e deixando em string
        if Room.objects.filter(code=code).count() == 0: # se não houver nenhum código gerado, da um break
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    convidado_pode_pausar = models.BooleanField(default=False)
    pedido_para_pular = models.IntegerField(null=False, default=1)
    criado_em = models.DateTimeField(auto_now_add=True) # para adicionar a hora exata em que foi criado a sala
    
    