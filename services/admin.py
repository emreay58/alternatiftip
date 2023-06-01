from django.contrib import admin
from .models import Hacamat,SulukTedavisi,PrpTedavisi,OzonTedavisi

class HacamatAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields =('slug',)


class SulukAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields =('slug',)


class PrpAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields =('slug',)


class OzonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields =('slug',)

admin.site.register(Hacamat, HacamatAdmin)
admin.site.register(SulukTedavisi, SulukAdmin)
admin.site.register(PrpTedavisi, PrpAdmin)
admin.site.register(OzonTedavisi, OzonAdmin)


# Register your models here.

