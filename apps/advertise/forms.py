from django import forms

from semanticuiform.widgets import SemanticSearchSelect, SemanticSearchSelect

from apps.advertise.models import County
from .models import Advertise


class AdvertiseForm(forms.ModelForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not kwargs.get('data'):
            self.fields['county'].queryset = County.objects.none()

    class Meta:
        model = Advertise
        exclude = ('user', 'state', 'expiration_date')
        widgets = {
            'major': SemanticSearchSelect,
            'county': SemanticSearchSelect,
            'university': SemanticSearchSelect,
        }
