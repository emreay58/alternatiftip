from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


# Create your models here.

class Hacamat(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hacamat/')
    ilkaciklama = models.TextField()
    descriptions = RichTextUploadingField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)


class SulukTedavisi(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='suluk/')
    ilkaciklama = models.TextField()
    descriptions = RichTextUploadingField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)


class PrpTedavisi(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='prp/')
    ilkaciklama = models.TextField()
    descriptions = RichTextUploadingField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)


class OzonTedavisi(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ozon/')
    ilkaciklama = models.TextField()
    descriptions = RichTextUploadingField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)




