from django.urls import path
from .views import BookingCreateView, ItemListView, AreaListView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='service-list'),
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('book/', BookingCreateView.as_view(), name='book-service'),
]