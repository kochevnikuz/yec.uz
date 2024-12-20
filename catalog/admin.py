from django.contrib import admin
from .models import Collection, Carpet, TypeCarpet
from django.utils.safestring import mark_safe

# Register your models here.

class CarpetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'watched', 'is_published', 'collection', 'created_at', 'update_at', 'get_image')
    list_display_links = ('id', 'code',)
    list_editable = ('is_published',)
    readonly_fields = ('watched', 'get_image')
    list_filter = ('collection', 'is_published',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px">')
        else:
            return 'нет картинки'

    get_image.short_description = 'Миниатюра'

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'is_published', 'created_at', 'get_image')
    list_display_links = ('id', 'name',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'type', 'created_at',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50px">')
        else:
            return 'нет картинки'

    get_image.short_description = 'Миниатюра'

admin.site.register(TypeCarpet)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Carpet, CarpetAdmin)

