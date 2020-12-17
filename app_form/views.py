from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from . forms import (TdtProductForm, CdtProductColorForm,
PhotoInLineFormSet, CdtProductPhotoForm, TdtSkuProductForm)
#, TdtSkuProductForm, ProductSkuProductForm
#from django.urls import reverse
from . models import (TdtProduct, CdtColor, CdtProductPhoto, 
CdtProductColor, TdtSkuProduct)
from django.forms.models import inlineformset_factory

def home(request):
    products = TdtProduct.objects.all()
    color = CdtProductColor.objects.all()
    sku = TdtSkuProduct.objects.all()
    

    context = {
        'products':products,
        'color':color,
        'sku':sku,
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


def createColorPhoto(request, pk):
    print(pk)
    id_product = pk

    #Llamar al primer form
    form_one = CdtProductColorForm(initial={'id_product':id_product})
    #Llamar al segundo form
    #form_two = CdtProductPhotoForm

    #ColorInLineFormSet = inlineformset_factory(CdtProductColor, CdtProductPhoto, form=CdtProductPhotoForm)
    #ColorInLineFormSet = inlineformset_factory(CdtProductColor, CdtProductPhoto, fields=('id_product','id_color'))

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
        #'form_two':form_two,
        'formset':formset,
    }

    return render(request, 'colorphoto.html', context)
    


def updateColorPhoto(request, pk):
    
    
    
    pcolor = CdtProductColor.objects.get(id=pk)
    


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
    }
    return render(request, 'colorphoto.html', context)


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

def deleteProductColor(request, pk):
    pcolor = CdtProductColor.objects.get(id=pk)

    if request.method == 'POST':
        pcolor.delete()
        return redirect(home)

    context = {
        'pcolor':pcolor
    }

    return render(request, 'delete-pcolor.html', context)


def deleteProduct(request, pk):
    products = TdtProduct.objects.get(id=pk)
    if request.method == "POST":
        products.delete()
        return redirect('/')
    
    context = {
        'products':products,
    }
    
    return render(request, 'delete.html', context)


def createProductSku(request, pk_one, pk_two):

    id_product = int(pk_one)
    id_pc = int(pk_two)
    
    #print(id_product + '***********')
    #print(pk_one + '===========')
    #Llamar al primer form
    form = TdtSkuProductForm(initial={
        'id_product_color':id_pc,
        'id_product':id_product,
    })
    #Llamar al segundo form
    #form_two = CdtProductPhotoForm

    #ColorInLineFormSet = inlineformset_factory(CdtProductColor, CdtProductPhoto, form=CdtProductPhotoForm)
    #ColorInLineFormSet = inlineformset_factory(CdtProductColor, CdtProductPhoto, fields=('id_product','id_color'))

    #form = CdtProductColorForm()
    #formset = PhotoInLineFormSet()


    if request.method == 'POST':
        form = TdtSkuProductForm(request.POST)
        #Si la informacion del formulario es valido
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
    }

    return render(request, 'sku.html', context)

