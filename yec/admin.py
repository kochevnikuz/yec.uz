from django.contrib import admin
from .models import Slide
from django.utils.safestring import mark_safe


# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at', 'get_image')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('created_at', 'is_published',)
    fields = ('id', 'title', 'is_published', 'created_at', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80px">')
        else:
            return 'нет картинки'

    get_image.short_description = 'Миниатюра'

admin.site.register(Slide, SlideAdmin)