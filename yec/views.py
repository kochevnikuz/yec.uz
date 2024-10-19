from django.db.models.functions import RowNumber
from django.shortcuts import render
from django.db.models import OuterRef, Subquery, Count, Window, F
from catalog.models import Collection, Carpet
from yec.models import Slide


# Create your views here.
def index(request):
    sliders = Slide.objects.all()

    context = {
        'sliders': sliders,
    }

    return render(request, template_name='yec/index.html', context=context)

def about_page(request):
    return render(request, template_name='yec/about.html')