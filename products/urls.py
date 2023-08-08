from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from products.views import ProductViewSet,ReviewViewSet,CommentViewSet, ProQuestViewSet
from django.views.static import serve
from django.urls import re_path
from elderly.settings import MEDIA_ROOT


router = DefaultRouter()
router.register('product', ProductViewSet) 
router.register('review', ReviewViewSet)
router.register('comment', CommentViewSet)
router.register('quest', ProQuestViewSet)

urlpatterns = [
    #라우터
    path('router/', include(router.urls)), 
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
]