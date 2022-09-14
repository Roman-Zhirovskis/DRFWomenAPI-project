from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView,)

from women.views import *
from women.customrouters import *

# router = routers.DefaultRouter()
# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename='women')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),
#     # path('api/v1/women/pk', )
# ]
#
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # new
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # new
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # new
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]


