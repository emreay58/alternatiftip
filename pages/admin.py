from doctest import master
from pyexpat import model
from django.contrib import admin
from .models import RandevuModel, ServicesField, MessageModel, PicturesModel

# Register your models here.

class RandevuAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','mesage',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields =('slug',)


admin.site.register(RandevuModel, RandevuAdmin)
admin.site.register(ServicesField, ServicesAdmin)
admin.site.register(MessageModel)
admin.site.register(PicturesModel)








