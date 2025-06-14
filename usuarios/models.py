# usuarios/models.py - VERSÃO FINAL SEM ERROS DE SINTAXE

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Usuario(AbstractUser):
    # 1. Removemos os campos que não usaremos.
    first_name = None
    last_name = None

    # 2. Definimos nossas escolhas para o tipo de usuário.
    TIPO_USUARIO_CHOICES = [
        ('CLIENTE', 'Cliente'),
        ('CORRETOR', 'Corretor'),
    ]

    # 3. Definimos nossos campos personalizados.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, verbose_name="Tipo de Usuário", blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    
    # 4. Redefinimos o email para garantir que seja único.
    email = models.EmailField(unique=True, verbose_name="Endereço de e-mail")

    # 5. Dizemos ao Django para usar o email para login.
    USERNAME_FIELD = 'email'
    
    # 6. Definimos os campos obrigatórios ao criar um superusuário.
    REQUIRED_FIELDS = ['username']

    # 7. MÉTODOS DE VERIFICAÇÃO DE TIPO DE USUÁRIO
    @property
    def is_corretor(self):
        """Retorna True se o usuário for do tipo CORRETOR."""
        return self.tipo_usuario == 'CORRETOR'

    @property
    def is_cliente(self):
        """Retorna True se o usuário for do tipo CLIENTE."""
        return self.tipo_usuario == 'CLIENTE'

    def __str__(self):
        """Representação em string do objeto."""
        return self.email