from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name