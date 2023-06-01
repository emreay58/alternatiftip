
from email.mime import image
from turtle import title
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ServicesField(models.Model):
    image = models.ImageField(upload_to='hizmetler')
    title = models.CharField(max_length=50)
    kisaaciklama = models.CharField(max_length=255)
    description = RichTextUploadingField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f"/{self.slug}"
    


class RandevuModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    tarih = models.CharField(max_length=10)
    bolum = models.CharField(max_length=50)
    mesage = models.TextField()


    def __str__(self):
        return self.name


class MessageModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    konu = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class PicturesModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="galery/")
  
    def __str__(self):
        return self.name

    
    






