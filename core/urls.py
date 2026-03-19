from rest_framework.routers import DefaultRouter
from .views import Rideviewset
from django.urls import path, include


router=DefaultRouter()
router.register('rides',Rideviewset)
urlpatterns = [
    path('', include(router.urls))
]