from django.urls import path, include
from cart.views  import CartView, CartViewSet, OptionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('option',OptionViewSet)


urlpatterns = [
    path('', CartView.as_view()),
    path('router/', include(router.urls)),
]