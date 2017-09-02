from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(
            default=timezone.now)
    publicado_en = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publicado_en = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

# Create your models here.
