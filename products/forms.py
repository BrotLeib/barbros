import re

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Product
##########################################################################

class SearchForm(forms.Form):
    key = forms.CharField(max_length=6, min_length=6)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'key',
            'zip_code',
            'type',)

    def clean_zip_code(self):
        pattern = re.compile("^[1-9]\d{4,6}$")
        if not pattern.match(self.cleaned_data['zip_code']):
            raise ValidationError(_('geben Sie einen gültige Postleitzahl an'))
        return self.cleaned_data['zip_code']


    def save(self, request, commit=True):
        product = super().save(commit=False)
        if not product.pk:
            product.slug = slugify(self.cleaned_data['type'] + self.cleaned_data['key'])
            product.profile = request.user.profile
        if commit:
            product.save()
        return product
