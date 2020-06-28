from django.db import models


# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)
    arquivo = models.ImageField(upload_to="media/pictures", blank=True)
    @property
    def image_url(self):
        if self.arquivo and hasattr(self.arquivo, 'url'):
            return self.arquivo.url    

class Meta:
        ordering = ['-created_on']
        def __str__(self):
            return '%s %s' % (self.titulo, self.data)


class Comment(models.Model):
    postagem = models.ForeignKey(Postagem,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

        # return '%s %s' % (self.body, self.name)