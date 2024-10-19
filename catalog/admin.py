from django.contrib import admin
from .models import Collection, Carpet, TypeCarpet

# Register your models here.

class CarpetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'watched', 'is_published', 'collection', 'created_at', 'update_at')
    list_display_links = ('id', 'code',)
    list_editable = ('is_published',)
    readonly_fields = ('watched',)
    list_filter = ('collection', 'is_published',)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'is_published', 'created_at', 'image')
    list_display_links = ('id', 'name',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'type', 'created_at',)


admin.site.register(TypeCarpet)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Carpet, CarpetAdmin)

