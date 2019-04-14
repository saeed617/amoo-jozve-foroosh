from django import forms

from semanticuiform.widgets import SemanticSearchSelect, SemanticSearchSelect

from .models import Advertise


class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        exclude = ('user', 'state', 'expiration_date')
        widgets = {
            'major': SemanticSearchSelect,
            'county': SemanticSearchSelect,
            'university': SemanticSearchSelect,
        }
