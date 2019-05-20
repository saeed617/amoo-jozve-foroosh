from django import forms
from django.forms import inlineformset_factory

from semanticuiform.widgets import SemanticSearchSelect

from apps.advertise.models import County, AdvertiseImage
from .models import Advertise


class AdvertiseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
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


class AdvertiseImageForm(forms.ModelForm):
    class Meta:
        model = AdvertiseImage
        fields = ('image',)


AdvertiseImageFormSet = inlineformset_factory(Advertise, AdvertiseImage, form=AdvertiseImageForm, extra=1,
                                              can_delete=True)
