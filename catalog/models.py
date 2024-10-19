from django.db import models
from django.urls import reverse


# Create your models here.
class TypeCarpet(models.Model):
    name = models.CharField(max_length=32, verbose_name='Тип ковра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ковра'
        verbose_name_plural = 'Типы ковров'


class Collection(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(default='Описания коллекции', verbose_name='Описания', blank=True, null=True)
    image = models.ImageField(upload_to='photos/collections/%Y/%m/', verbose_name='photo Коллекции')
    type = models.ForeignKey(TypeCarpet, on_delete=models.CASCADE, verbose_name='Тип ковра')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:collection', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Carpet(models.Model):
    code = models.CharField(max_length=32, verbose_name='Код Ковра', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/carpets/%Y/%m/', blank=True, null=True, verbose_name='Изображения')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция',
                                   related_name='carpets')
    roll = models.BooleanField(default=False, verbose_name='Рулон')

    def save(self, *args, **kwargs):
        # Если имя товара не задано, берем его из имени файла изображения
        if not self.code and self.photo:
            # Извлекаем имя файла без расширения
            self.code = self.photo.name.split('/')[-1].split('.')[0]
        super(Carpet, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Ковер'
        verbose_name_plural = 'Ковры'
