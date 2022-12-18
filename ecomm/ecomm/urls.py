"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from pack.views import landpage
from django.conf import settings
from django.conf.urls.static import static




from pack.views import contact

from pack.views import collection
from pack.views import collectionview
from pack.views import productview
from pack.views import addtocart
from pack.views import viewcart

from pack.views import checkout
from pack.views import signupaction
from pack.views import loginpage
from pack.views import logoutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',  landpage,name="index"),

    path('collections/',collection,name="collections"),
    path('signup/', signupaction,name="signup"),
    path('login/',loginpage,name="loginpage"),
    path('logout/',logoutpage,name="logout"),
    
    path('cart',viewcart,name="cart"),
    
    path('<str:slug>',collectionview,name="collectionview"),
    path('<str:cate_slug>/<str:prod_slug>',productview,name="productview"),
    path('add-to-cart',addtocart,name="addtocart"),
    
    
    
    path('contact/',contact),
    path('checkout/',checkout,name="checkout"),
    
    
    
    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
