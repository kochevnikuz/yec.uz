from django.urls import path
from .views import *


app_name = 'yec'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about_page, name='about'),
]
