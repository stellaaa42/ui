from rest_framework import generics
from .models import Booking, Item, Area
from .serializers import BookingSerializer, ItemSerializer, AreaSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AreaListView(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def perform_create(self, serializer):
        # Custom logic before saving (e.g., logging, data transformation)
        booking = serializer.save()
        print(f"New booking created: {booking.name} for {booking.appointment_date} at {booking.appointment_time}")
