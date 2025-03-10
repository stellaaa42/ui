from .models import Booking, Service, Area
from .serializers import BookingSerializer, ServiceSerializer, AreaSerializer, BookingSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db import connection


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AreaListView(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Custom logic before saving (e.g., logging, data transformation)
        # booking = serializer.save(user=self.request.user)
        booking = serializer.save()
        print(f"New booking created: {booking.name} for {booking.appointment_date} at {booking.appointment_time}")

class BookingListView(generics.ListAPIView): 
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()
    
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})




