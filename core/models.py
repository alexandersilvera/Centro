from django.db import models

from stdimage.models import StdImageField

class Base(models.Model):
    created = models.DateField('Creado', auto_now_add=True)
    modified = models.DateField('Actualizado', auto_now=True)
    activo = models.BooleanField('Activo?', default=True)

    class Meta:
        abstract = True

class Video(Base):
    url = models.URLField(max_length=50)

