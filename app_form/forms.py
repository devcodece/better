from django import forms
from django.forms.models import inlineformset_factory
from . models import (TdtProduct, CdtProductColor, CdtProductPhoto,
TdtSkuProduct)
#from betterforms.multiform import MultiModelForm

class TdtProductForm(forms.ModelForm):
    class Meta:
        model = TdtProduct
        fields = [
            'tx_product_name',
            'tx_description',
            'id_category_person',
            'id_category',
            'id_subcategory',
            'id_brand',
            'id_vendor',
        ]
        widgets = {
            'tx_product_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }),
            'tx_description':forms.Textarea(attrs={
                'class':'form-control',
                'rows':2,
                'placeholder':'Product description...'
            }),
            'id_category_person':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_category':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_subcategory':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_brand':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_vendor':forms.Select(attrs={
                'class':'form-control'
            }),
        }

class CdtProductColorForm(forms.ModelForm):
    class Meta:
        model = CdtProductColor
        fields = [
            'id_product',
            'id_color',
        ]
        widgets = {
            'id_product':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_color':forms.Select(attrs={
                'class':'form-control'
            }),
        }

class CdtProductPhotoForm(forms.ModelForm):
    class Meta:
        model = CdtProductPhoto
        fields = [
            'tx_url_photo',
            'bl_primary',
        ]
        """ widgets = {
            'tx_url_photo':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'bl_primary':forms.CheckboxInput(attrs={
                'class':'form-control'
            }),
        } """

class TdtSkuProductForm(forms.ModelForm):
    class Meta:
        model = TdtSkuProduct
        fields = [
            'sku',
            'id_product',
            'id_product_color',
            'id_size',
            'quantity',
            'price',
        ]
        widgets = {
            'sku':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'id_product':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_product_color':forms.Select(attrs={
                'class':'form-control'
            }),
            'id_size':forms.Select(attrs={
                'class':'form-control'
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'min':'0'
            }),
            'price':forms.NumberInput(attrs={
                'class':'form-control',
                'min':'0'
            }),
        }

PhotoInLineFormSet = inlineformset_factory(CdtProductColor, 
CdtProductPhoto, form=CdtProductPhotoForm, can_delete=True)
