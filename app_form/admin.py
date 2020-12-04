from django.contrib import admin
from . models import CdtBrand, CdtVendor, TdtProduct, CdtProductPhoto, CdtColor
# Register your models here.

#admin.site.register(CdtSize)
admin.site.register(CdtVendor)
admin.site.register(CdtBrand)
admin.site.register(TdtProduct)
#admin.site.register(TdtSkuProduct)
admin.site.register(CdtProductPhoto)
admin.site.register(CdtColor)
