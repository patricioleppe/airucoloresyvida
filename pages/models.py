from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name="Pagina"
        verbose_name_plural="Paginas"
        # el - antes de created_at  es para darle orden descedente
        ordering = ["order","title"]
        
    def __str__(self):
        return self.title    