from django.db import models

# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)
    

class Meta:
        ordering = ['-created_on']
        def __str__(self):
            return '%s %s' % (self.titulo, self.data)

class Usuario(models.Model):
    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False),
    
    def __str__(self):
        return '%s %s' % (self.nome, self.email)