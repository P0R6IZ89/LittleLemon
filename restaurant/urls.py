from django.contrib import admin
from django.urls import path, include
from .views import BookingViewSet, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name="menu_item_list"),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    # booking urls are on project level
]
