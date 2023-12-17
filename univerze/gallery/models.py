from django.db import models

# Create your models here.
class project(models.Model):
    Title = models.CharField(max_length=200, verbose_name = "Título")
    Planet = models.CharField(max_length=100, verbose_name = "Planeta")
    Description = models.CharField(max_length=100, verbose_name = "Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    link = models.URLField(verbose_name="Enlace",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificación")

    def __str__(self) -> str:
        return self.Title

    class Meta:
        verbose_name = "galeria"
        verbose_name_plural = "galerias"
        ordering = ["-created"]