from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant.views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
