"""snapreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import handler404, handler500
from mainsite import views as mainsite_views
from shopify_install import views as shopify_install_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('record/', include('record.urls')),
    path('install.php', shopify_install_views.install, name='install'),
    path('generate_token.php', shopify_install_views.generate_token, name='generate_token'),
    path('functions.php', shopify_install_views.functions, name='functions'),
    path('api_call_write_products.php', shopify_install_views.api_call_write_products, name='api_call_write_products'),
    path('',include('mainsite.urls'))
]

handler404 = mainsite_views.error_404
handler500 = mainsite_views.error_500
