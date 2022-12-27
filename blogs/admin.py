from django.contrib import admin
from .models import Category, Blogs

# Register your models here.


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}

@admin.register(Category)
class CaetgoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields={'slug':('name',)}