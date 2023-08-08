from django.urls import path, include
from cart.views  import CartView, CartViewSet, OptionViewSet
from rest_framework import routers
from django.views.static import serve
from django.urls import re_path
from elderly.settings import MEDIA_ROOT

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('option',OptionViewSet)


urlpatterns = [
    path('', CartView.as_view()),
    path('router/', include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
]