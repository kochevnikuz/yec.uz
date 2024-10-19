from django import template
from catalog.models import Collection, Carpet

register = template.Library()


@register.simple_tag()
def get_all_collections():
    return Collection.objects.all().order_by('-created_at')

@register.simple_tag()
def get_all_collections_active():
    return Collection.objects.all().filter(is_published = True)