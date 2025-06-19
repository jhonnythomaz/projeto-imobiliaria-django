# usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        # Os campos que pediremos no formulário de cadastro.
        # O Django já cuida de pedir a senha e a confirmação de senha.
        fields = UserCreationForm.Meta.fields + ('telefone',)