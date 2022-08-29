from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet,convert_lead_to_client

router = DefaultRouter()
router.register('clients',ClientViewSet,basename='clients')
urlpatterns = [
    path('convert_lead_to_client/',convert_lead_to_client,name='convert_lead_to_client'),
    path('',include(router.urls))
]