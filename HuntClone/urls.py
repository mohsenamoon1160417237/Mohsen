"""HuntClone URL Configuration

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
import accounts.views
import products.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,accounts.views.home , name = "home"),
    path('accounts/signup/' , accounts.views.signup , name = "signup"),
    path('accounts/login/' , accounts.views.login , name = "login"),
    path('accounts/logout/' , accounts.views.logout , name = "logout"),
    path('products/create/' , products.views.create , name = "create" ),
    path('products/<int:product_id>/' , products.views.details , name = "details"),
    path('products/<int:product_id>/upvote/' , products.views.upvote , name = "upvote"),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
