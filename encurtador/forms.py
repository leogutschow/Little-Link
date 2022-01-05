from django import forms
from .models import Encurtador
from django.forms.models import ModelForm

class EncurtadorForm(ModelForm):

    def clean(self):
        data = super().clean()
        link_original = data.get('link_original')

    class Meta:
        model = Encurtador
        fields = ('link_original','link_encurtado')
        widgets = {
            'link_encurtado': forms.HiddenInput()
        }

