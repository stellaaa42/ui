from django.urls import path
from .views import BookingCreateView, ItemListView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='service-list'),
    path('book/', BookingCreateView.as_view(), name='book-service'),
]