"""better URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_form.views import (home, product_info, product_detail, 
createProduct, updateProduct, deleteProduct, createColorPhoto,
updateColorPhoto, deleteProductColor)
from django.conf.urls.static import static
from django.conf import settings
#NewProduct, Success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product-detail/<str:pk_test>/', product_detail, name='product-detail'),
    path('product-info', product_info, name='product-info'),

    #Create Product
    path('product-form', createProduct, name='product-form'),
    #Update Product
    path('update-product/<str:pk>/', updateProduct, name='update-product'),
    #Delete Product
    path('delete-product/<str:pk>/', deleteProduct, name='delete-product'),


    #Add Photo
    path('create-photo/<str:pk>', createColorPhoto, name='create-photo'),
    #Update Photo
    path('update-photo/<str:pk>', updateColorPhoto, name='update-photo'),
    #Delete ProductColor
    path('delete-pcolor/<str:pk>', deleteProductColor, name='delete-pcolor'),

    #path('success', Success.as_view(), name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
