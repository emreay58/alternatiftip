from django.contrib import admin
from .models import ServicesField,PicturesModel,RandevuModel,MessageModel

# Register your models here.


@admin.register(ServicesField)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}


@admin.register(RandevuModel)
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PicturesModel)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name',)
 








