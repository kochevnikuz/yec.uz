from django.db import models
# from django.urls import reverse


# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=32, verbose_name='Наименования')
    image = models.ImageField(upload_to='photos/sliders/%Y/%m/', verbose_name='Изображения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'