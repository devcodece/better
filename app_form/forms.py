from django.forms import ModelForm
from . models import (TdtProduct, CdtProductColor,
CdtProductPhoto)
from django.forms.models import inlineformset_factory
#from betterforms.multiform import MultiModelForm

class TdtProductForm(ModelForm):
    class Meta:
        model = TdtProduct
        fields = '__all__'

class CdtProductColorForm(ModelForm):
    class Meta:
        model = CdtProductColor
        fields = '__all__'

class CdtProductPhotoForm(ModelForm):
    class Meta:
        model = CdtProductPhoto
        exclude = ('id_product_color',)

PhotoInLineFormSet = inlineformset_factory(CdtProductColor, 
CdtProductPhoto, form=CdtProductPhotoForm, can_delete=True)


#class TdtSkuProductForm(ModelForm):
    #class Meta:
        #model = TdtSkuProduct
        #fields = ['sku','id_size','quantity','price']

#class ProductSkuProductForm(MultiModelForm):
    #form_classes = {
        #'product':TdtProductForm,
        #'sku':TdtSkuProductForm,
    #}