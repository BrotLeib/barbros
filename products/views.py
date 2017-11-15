from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import error
from django.utils.translation import ugettext as _

from .models import Product
from .forms import SearchForm, ProductForm


class HomeView(View):
    template_name = 'organizer/index.html'
    model = Product
    form_class = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            try:
                key = bound_form.cleaned_data['key']
                product = self.model.objects.get(key=key)
                return redirect(product.get_absolute_url())
            except ObjectDoesNotExist:
                error(request, _('Produkt konnte nicht gefunden werden. Versuche es doch erneut!'))
                return render(request, self.template_name, {'form': self.form_class(request.POST)})
        else:
            error(_('unbekannter Fehler'))
            return render(request, self.template_name, {'form': self.form_class(request.POST)})

class ProductCreate(View):
    model = Product
    form_class = ProductForm
    template_name = 'profiles/product_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form = bound_form.save(request)
            return redirect(bound_form.profile)
        else:
            return render(request, self.template_name, {'form': bound_form})


class ProductDetail(DetailView):
    model = Product
