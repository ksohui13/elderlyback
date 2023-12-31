from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import re_path
from elderly.settings import MEDIA_ROOT
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/products/', include('products.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
