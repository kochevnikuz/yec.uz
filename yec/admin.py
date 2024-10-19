from django.contrib import admin
from .models import Slide


# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('created_at', 'is_published',)

admin.site.register(Slide, SlideAdmin)