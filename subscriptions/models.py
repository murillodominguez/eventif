from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscricao'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name