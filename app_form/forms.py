from django.forms import ModelForm
from . models import (TdtProduct, CdtProductColor, CdtProductPhoto,
TdtSkuProduct)
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

class TdtSkuProductForm(ModelForm):
    class Meta:
        model = TdtSkuProduct
        fields = '__all__'

PhotoInLineFormSet = inlineformset_factory(CdtProductColor, 
CdtProductPhoto, form=CdtProductPhotoForm, can_delete=True)

#SkuInLineFormSet = inlineformset_factory(TdtSkuProduct, 
#form=TdtSkuProductForm, can_delete=True)
