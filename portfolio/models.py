from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200, verbose_name = "Title")
    description= models.TextField(verbose_name = "description")
    image= models.ImageField(verbose_name = "image", upload_to = "projects")
    link= models.URLField(verbose_name = "Web Address", null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name = "Creation date")
    updated= models.DateTimeField(auto_now=True, verbose_name = "Edition date")

    class Meta:
        verbose_name = "proyect"
        verbose_name_plural = "proyects"
        ordering = ["-created"]

    def __str__(self):
        return self.title