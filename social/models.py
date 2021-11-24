from django.db import models

# Create your models here.
class Link(models.Model):
    
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name="Enlace"
        verbose_name_plural="Enlaces"
        # el - antes de created_at  es para darle orden descedente
        ordering = ["name"]
        
    def __str__(self):
        return self.name    