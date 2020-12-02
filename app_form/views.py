from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from . forms import ProductSkuProductForm
from django.urls import reverse
from . models import TdtProduct

# Create your views here.

class NewProduct(CreateView):
    model = TdtProduct
    form_class = ProductSkuProductForm
    template_name = 'form-product.html'

    def from_valid(self, form):
        product = form['product'].save()
        sku = form['sku'].save(commit=False)
        sku.product = product
        sku.save()
        return HttpResponseRedirect(reverse('success'))

class Success(TemplateView):
    template_name = 'success.html'

