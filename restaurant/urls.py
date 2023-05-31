from django.contrib import admin
from django.urls import path, include
from .views import BookingViewSet, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
