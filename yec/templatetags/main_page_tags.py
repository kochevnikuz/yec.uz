from django import template
from django.db.models import Window, F
from django.db.models.functions import RowNumber

from catalog.models import Collection, Carpet
from yec.models import Slide

register = template.Library()


@register.simple_tag()
def get_new_carpets():
    # Используем оконную функцию для нумерации ковров в пределах каждой коллекции
    return Carpet.objects.annotate(
        row_number=Window(
            expression=RowNumber(),
            partition_by=[F('collection')],  # Разбиваем на "окна" по коллекциям
            order_by=F('created_at').desc()  # Сортируем по дате создания (от новых к старым)
        )
    ).filter(row_number__lte=2)  # Оставляем только 2 ковра из каждой коллекции