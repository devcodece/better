from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from . forms import TdtProductForm
#, TdtSkuProductForm, ProductSkuProductForm
from django.urls import reverse
from . models import TdtProduct, CdtColor, CdtProductPhoto, CdtProductColor
from django.forms import BaseInlineFormSet, inlineformset_factory

def home(request):
    products = TdtProduct.objects.all()
    color = CdtProductColor.objects.all()
    #color = photo.id_product_color.all()
    #photos = color.id_photo.all()
    #photos_primary = photos.filter(bl_primary=True)
    

    context = {
        'products':products,
        'colors':color,
        #'color':color,
    }
    #print(photo)

    return render(request, 'dashboard.html', context)

def color_photo(request):
    return render(request, 'color-photo.html')

def product_info(request):
    products = TdtProduct.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'product-info.html', context)

def product_detail(request, pk_test):
    product_color = CdtProductColor.objects.get(id=pk_test)
    #product = product_color.id_product.all()
    photo = product_color.cdtproductphoto_set.all()
    sku = product_color.tdtskuproduct_set.all()
    sku_count = sku.count()
    first = sku.first()
    #print(price)
    
    context = {
        'product':product_color,
        #'product':product,
        'photo':photo,
        'sku':sku,
        'sku_count':sku_count,
        'first':first,
    }
    return render(request, 'product-detail.html', context)

def createProduct(request):
    #Llama de TdtProductForm
    form = TdtProductForm()

    #obtener los datos que se envian por POST
    if request.method == 'POST':
        form = TdtProductForm(request.POST)
        #Si la informacion del formulario es valido
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }

    return render(request, 'product_form.html', context)

def updateProduct(request, pk):
    products = TdtProduct.objects.get(id=pk)
    form = TdtProductForm(instance=products)

    if request.method == 'POST':
        form = TdtProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form,
        }

    return render(request, 'product_form.html', context)

def deleteProduct(request, pk):
    context = {
        '':
    }

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

