from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from . forms import TdtProductForm
#, TdtSkuProductForm, ProductSkuProductForm
from django.urls import reverse
from . models import TdtProduct
from django.forms import BaseInlineFormSet, inlineformset_factory

def home(request):
    return render(request, 'dashboard.html')

def color_photo(request):
    return render(request, 'color-photo.html')

def product_info(request):
    return render(request, 'product-info.html')

def sku(request):
    return render(request, 'sku.html')


#class NewProduct(CreateView):
    #model = TdtProduct
    #form_class = ProductSkuProductForm
    #template_name = 'form-product.html'

    #def form_valid(self, form):
        #product = form['product'].save()
        #sku = form['sku'].save(commit=False)
        #print(product + '====================')
        #sku.id_product = product
        #sku.save()
        #return HttpResponseRedirect(reverse('success'))

#def create(request):
    #TdtProductInLineFormSet = inlineformset_factory(TdtProduct, TdtSkuProduct, form=TdtProductForm)
    #productForm = TdtProductForm(request.POST)






#class Success(TemplateView):
    #template_name = 'success.html'

