from .models import Booking, Item, Area
from .serializers import BookingSerializer, ItemSerializer, AreaSerializer, BookingSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AreaListView(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class BookingCreateView(generics.CreateAPIView):  # ✅ Only allows POST (no GET)
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Book list"}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "Booking created successfully!"}, status=status.HTTP_201_CREATED)
 
class UserBookingListView(generics.ListAPIView):  # ✅ Only allows users to see their own bookings
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # ✅ Requires login to see bookings

    def get_queryset(self):
        """Return only bookings that belong to the logged-in user."""
        return Booking.objects.filter(user=self.request.user)  # ✅ Only return user's own bookings
    
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})



