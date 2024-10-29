from django import forms
from .models import Carpet


class CarpetAddForm(forms.ModelForm):


    class Meta:
        model = Carpet
        fields = ['code', 'photo', 'is_published', 'collection']