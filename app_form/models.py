from django.db import models

# Create your models here.

class CdtBrand(models.Model):
    tx_brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.tx_brand_name

class CdtVendor(models.Model):
    tx_name_vendor = models.CharField('Vendor', max_length=50)
    nm_phone_number_vendor = models.CharField('Phone Number', max_length=10, blank=True, null=True)
    tx_description = models.CharField('Description', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.tx_name_vendor


class TdtProduct(models.Model):
    #GENDER_CHOICES = [
    #    ('0', 'Gender'),
    #    ('1', 'Male'),
    #    ('2', 'Female'),
    #    ('3', 'Other'),
    #]

    tx_product_name = models.CharField('Product Name', max_length=75)
    tx_description = models.TextField('Description', max_length=300)
    #id_category_person = models.ForeignKey(CdtCategoryPerson, on_delete=models.CASCADE, null=True)
    #nm_sale_unit = models.DecimalField(max_digits=8, decimal_places=2)
    #id_category = models.ForeignKey(CdtCategory, on_delete=models.CASCADE, null=True)
    #id_subcategory = models.ForeignKey(CdtSubcategory, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(CdtBrand, on_delete=models.CASCADE)
    id_vendor = models.ForeignKey(CdtVendor, on_delete=models.CASCADE)
    #id_color = models.ManyToManyField(CdtColor)
    #size = models.ForeignKey(CdtSize, on_delete=models.CASCADE, blank=True, null=True)
    #id_photo = models.ManyToManyField(CdtProductPhoto)
    #img_photo2 = models.ImageField(null=True, blank = True)
    #img_photo3 = models.ImageField(null=True, blank = True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.tx_product_name


class CdtSize(models.Model):
    size = models.CharField('Size', max_length=4)
    #id_category = models.ForeignKey(CdtCategory, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'
    
    def __str__(self):
        return self.size

class TdtSkuProduct(models.Model):
    sku = models.CharField('Sku', max_length=75)
    id_product = models.ForeignKey(TdtProduct, on_delete=models.PROTECT)
    #id_product_color = models.ForeignKey(CdtColor, on_delete=models.PROTECT)
    id_size = models.ForeignKey(CdtSize, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Quantity')
    price = models.DecimalField('Price', max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'SKU Product'
        verbose_name_plural = 'SKU Products'
    
    def __str__(self):
        return self.sku