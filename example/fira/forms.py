from django import forms
from croppie.fields import CroppieField

from fira.models import Fira


class FiraForm(forms.ModelForm):
    image = CroppieField()

    image = CroppieField(
        options={
            'viewport': {
                'width': 300,
                'height': 300,
            },
            'boundary': {
                'width': 600,
                'height': 600,
            }
            ,
            'showZoomer': False,
            'enableResize': True,
            'enableOrientation': True,
            'mouseWheelZoom': 'ctrl'
        },
    )


    class Meta:
        model = Fira
        fields = ['image']
