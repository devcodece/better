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

#HIERARCHY JANGO
#first python
#second django
#third own

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from app_form.views import (home, createProduct, updateProduct, deleteProduct, 
                    createColorPhoto, updateColorPhoto, deleteProductColor, 
                    createProductSku, updateSku, deleteSku)
#NewProduct, Success
from user.views import Login, logoutUser


app_name = 'app_form'

urlpatterns = [
    path('admin/', admin.site.urls),
    #Ruta protegida
    path('', login_required(home), name='home'),

    #Create Product
    path('create-product', createProduct, name='create-product'),
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

    #Add SKU
    #Detail-SKU
    path('create-sku/<int:pk_one>/<int:pk_two>', createProductSku, name='create-sku'),
    #Update SKU
    path('update-sku/<slug>', updateSku, name='update-sku'),
    #Delete SKU
    path('delete-sku/<slug>', deleteSku, name='delete-sku'),



    #LOGIN
    path('accounts/login/', Login.as_view(), name='login'),
    #LOGOUT
    path('logout', login_required(logoutUser), name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
