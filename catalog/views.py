from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Collection, Carpet
from .forms import CarpetAddForm

# Create your views here.
def show_catalog(request):
    context = {
        'title': 'YEC GILAM',
    }

    return render(request, template_name='catalog/catalog.html', context=context)


def show_collection_carpets(request, pk):
    carpets = Carpet.objects.filter(collection_id=pk).order_by('-created_at')
    collection_active = Collection.objects.get(id=pk)

    context = {
        'title': collection_active.name,
        'carpets': carpets,
        'collection_active': collection_active,
    }

    return render(request, template_name='catalog/collection.html', context=context)

def carpets_by_date(request, year, month, collection_active_id):
    carpets = Carpet.objects.filter(created_at__year=year, created_at__month=month)
    collection = Collection.objects.get(id=collection_active_id)

    context = {
        'carpets': carpets,
        'collection_active': collection,
        'year': year,
        'month': month,
    }
    # Возвращаем результат в шаблон
    return render(request, 'catalog/carpets_by_date.html', context=context)

def add_carpet(request):
    if request.method == 'POST':
        pass
    else:
        form = CarpetAddForm()

    context = {
        'form': form,
        'title': 'Добавить Ковер'
    }

    return render(request, template_name='catalog/carpet_add_page.html', context=context)