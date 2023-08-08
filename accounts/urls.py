from django.urls import include, path
from . import views
from django.views.static import serve
from django.urls import re_path
from elderly.settings import MEDIA_ROOT

urlpatterns = [
    #일반 로그인, 회원가입
    path('signup/', views.UserCreate.as_view()), #회원가입
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
]