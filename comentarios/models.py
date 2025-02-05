from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    @property
    def nome_completo(self):
        return f"O usuario {self.usuario.first_name} entrou no site as {self.data}"

    def __str__(self):
        return self.usuario.username


