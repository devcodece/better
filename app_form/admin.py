from django.contrib import admin
from . models import CdtBrand, CdtVendor, CdtSize, TdtProduct, TdtSkuProduct
# Register your models here.

admin.site.register(CdtSize)
admin.site.register(CdtVendor)
admin.site.register(CdtBrand)
admin.site.register(TdtProduct)
admin.site.register(TdtSkuProduct)