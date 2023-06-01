from django.contrib import admin
from .models import Category, Blogs

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","yazar","slug")
    search_filters = ("title", "description",)
    readonly_fields = ("slug",)
    list_filter = ("tarih",)

admin.site.register(Category)
admin.site.register(Blogs, BlogAdmin)