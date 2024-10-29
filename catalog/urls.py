from django.urls import path
from .views import *


app_name = 'catalog'
urlpatterns = [
    path('', show_catalog, name='catalog'),
    path('collection/<int:pk>', show_collection_carpets, name='collection'),
    path('carpets/<int:year>/<int:month>/<int:collection_active_id>', carpets_by_date, name='carpets_by_date'),
    path('carpet/add/', add_carpet, name='add_carpet'),
]
