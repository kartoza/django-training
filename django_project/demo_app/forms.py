__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '05/06/16'

from django.contrib.gis import forms
from demo_app.models import InterestZone
from leaflet.forms.widgets import LeafletWidget


class InterestZoneForm(forms.ModelForm):

    class Meta:
        model = InterestZone
        exclude = []
        widgets = {'geometry': LeafletWidget(
            attrs={'map_width': 800, 'map_height': 500})}
