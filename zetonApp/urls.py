from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('kursant', KursantView)
router.register('instruktor', InstruktorView)
router.register('kurs', KursView)
router.register('zeton', ZetonView)

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]