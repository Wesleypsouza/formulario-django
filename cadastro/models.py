from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.TextField(max_length=20, blank=True, null=True)
    nascimento = models.DateField()

    def __str__(self):
        return self.email