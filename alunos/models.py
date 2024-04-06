from django.db import models
from django.core.validators import EmailValidator


class Aluno(models.Model):

    nome = models.CharField(max_length=20, null=False, blank=False)

    sobre_nome = models.CharField(max_length=50, null=False, blank=False)

    email = models.EmailField(
        max_length=70,
        null=False,
        blank=False,
        unique=True,
        validators=[EmailValidator(message="Email inválido.")],
    )

    data_nascimento = models.DateTimeField(null=False, blank=False)

    data_cadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = "aluno"
        indexes = [
            models.Index(fields=["email"], name="emai_idx"),
        ]

    def __str__(self) -> str:
        return self.nome
