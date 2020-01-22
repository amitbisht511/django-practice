from django.db import models
from django_extensions.db.models import AutoSlugField


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255, verbose_name="movie_title", unique=True)
    slug = AutoSlugField(populate_from="name")
    release_date = models.DateField(verbose_name="Release Date")
    description = models.TextField(
        verbose_name="Movie Description", blank=True, default=""
    )
    image = models.ImageField(upload_to='movies', null=True)
