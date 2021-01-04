from django.shortcuts import render, redirect
from django.forms.models import inlineformset_factory
from . models import (TdtProduct, CdtColor, CdtProductPhoto, 
CdtProductColor, TdtSkuProduct)
from . forms import (TdtProductForm, CdtProductColorForm,
PhotoInLineFormSet, CdtProductPhotoForm, TdtSkuProductForm)


def home(request):
    products = TdtProduct.objects.all().order_by('-id')[:3]
    color = CdtProductColor.objects.all().order_by('-id')[:3]
    sku = TdtSkuProduct.objects.all().order_by('create_date')[:5][::-1]

    context = {
        'products':products,
        'color':color,
        'sku':sku,
    }

    return render(request, 'dashboard.html', context)


###CRUD PRODUCT-BASE
def createProduct(request):
    #Llama de TdtProductForm
    form = TdtProductForm(initial={'id_category_person':1,
                'id_category':1,
                'id_subcategory':3,
                'id_brand':1,
                'id_vendor':1
                })

    #obtener los datos que se envian por POST
    if request.method == 'POST':
        form = TdtProductForm(request.POST)
        #Si la informacion del formulario es valido
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form,
    }

    return render(request, 'catalog/mcreate-product.html', context)


def updateProduct(request, pk):
    products = TdtProduct.objects.get(id=pk)
    form = TdtProductForm(instance=products)
    kword = pk

    if request.method == 'POST':
        form = TdtProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form':form,
        'kw':kword,
        }

    return render(request, 'catalog/mupdate-product.html', context)


def deleteProduct(request, pk):
    products = TdtProduct.objects.get(id=pk)
    if request.method == "POST":
        products.delete()
        return redirect('home')
    
    context = {
        'products':products,
    }
    
    return render(request, 'catalog/mdelete-product.html', context)


###CRUD PRODUCT COLOR-PHOTO
def createColorPhoto(request, pk):
    print(pk)
    id_product = pk

    form_one = CdtProductColorForm(initial={'id_product':id_product, 'id_color':1})

    form = CdtProductColorForm()
    formset = PhotoInLineFormSet()

    if request.method == 'POST':
        form = CdtProductColorForm(request.POST)
        formset = PhotoInLineFormSet(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save() 
            if formset.is_valid():
                formset.instance = photo
                formset.save()
                return redirect('home')

    context = {
        'form_one':form_one,
        'formset':formset,
        'kw':id_product,
    }

    return render(request, 'catalog/mcreate-photo.html', context)


def updateColorPhoto(request, pk):    
    pcolor = CdtProductColor.objects.get(id=pk)
    keyword = pk
    
    form_one = CdtProductColorForm(instance=pcolor)
    formset = PhotoInLineFormSet(instance=pcolor)

    if request.method == 'POST':
        form_one = CdtProductColorForm(request.POST, request.FILES, instance=pcolor)
        formset = PhotoInLineFormSet(request.POST, request.FILES, instance=pcolor)

        if form_one.is_valid():
            pcolor = form_one.save(commit=False)
            pcolor.save()

            if formset.is_valid():
                formset.instance = pcolor
                formset.save()

                return redirect('home')
    
    context = {
        'form_one':form_one,
        'formset':formset,
        'kw':keyword,
    }
    return render(request, 'catalog/mupdate-photo.html', context)


def deleteProductColor(request, pk):
    pcolor = CdtProductColor.objects.get(id=pk)

    if request.method == 'POST':
        pcolor.delete()
        return redirect('home')

    context = {
        'pcolor':pcolor
    }

    return render(request, 'catalog/mdelete-pcolor.html', context)


###CRUD PRODUCT SKU
def createProductSku(request, pk_one, pk_two):
    id_pc = pk_one
    id_product = pk_two

    form = TdtSkuProductForm(initial={
        'id_product_color':id_pc,
        'id_product':id_product,
        'id_size':1,

    })

    if request.method == 'POST':
        form = TdtSkuProductForm(request.POST)
        #Si la informacion del formulario es valido
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form,
        #'sku':sku,
        'id_pc':id_pc,
        'id_product':id_product,
    }

    return render(request, 'catalog/mcreate-sku.html', context)


def updateSku(request, slug):
    kw = TdtSkuProduct.objects.get(sku=slug)
    form = TdtSkuProductForm(instance=kw)
    kword = slug

    if request.method == 'POST':
        form = TdtSkuProductForm(request.POST, instance=kw)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form':form,
        'kw':kword,
        }

    return render(request, 'catalog/mupdate-sku.html', context)


def deleteSku(request, slug):
    kw = TdtSkuProduct.objects.get(sku=slug)

    if request.method == "POST":
        kw.delete()
        return redirect('home')
    
    context = {
        'kw':kw,
    }
    
    return render(request, 'catalog/mdelete-sku.html', context)