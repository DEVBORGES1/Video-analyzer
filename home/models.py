from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.FileField(upload_to="Video/")
    transcricao = models.TextField(null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo