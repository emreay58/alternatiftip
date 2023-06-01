from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, db_index=True, blank=True, unique=True, editable=False)

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug  = slugify(self.name)
        super().save(*args, **kwargs)
        

class Blogs(models.Model):
    image = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=100)
    descriptionbaslik = models.TextField(max_length=255)
    description = RichTextUploadingField()
    yazar = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tarih = models.DateField(auto_now_add=True)
    zaman = models.DateField(auto_now=True)
    slug = models.SlugField(null=False, blank=True,unique=True, editable=False)
    category = models.ManyToManyField(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}"
    