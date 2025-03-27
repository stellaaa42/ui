from .models import Booking, Service, Area, EmailVerify
from .serializers import (BookingSerializer, 
                            ServiceSerializer, AreaSerializer,
                            EmailVerifySerializer)
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import uuid
import logging


logger = logging.getLogger(__name__)

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
   
@method_decorator(csrf_exempt, name='dispatch')
class SubView(APIView):
    def post(self, request):

        logger.info("POST request:")
        logger.info(f"Request data: {request.data}")
        
        serializer = EmailVerifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                email = request.data.get('email')
                if not email:
                    return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
                
                sub = EmailVerify.objects.filter(email=email).first()
                # sub, created = EmailVerify.objects.get_or_create(email=email)
                # if not created:
                #     if getattr(sub, 'verified', False):
                #         return Response({'message': 'Email already verified'}, status=status.HTTP_200_OK)
                    # sub.token = uuid.uuid4()  # Regenerate token if unverified
                    # sub.save()

                verification_link = f"{settings.SITE_URL}/api/verify/?email={email}&token={sub.token}"
                print(f"Verification link: {verification_link}")

                try:
                    send_mail(
                        subject='Confirm Your Email',
                        message=f'Please confirm your email by clicking the link: {verification_link}',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=False,
                    )
                except Exception as e:
                    logger.error(f"Error sending email: {str(e)}")
                    return Response(
                        {'error': 'Failed to send verification email. Please try again later.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )            
                    
                return Response({'status': 'success', 'message': 'Please check your email to confirm'}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.exception("NO email")
                return Response(
                    {'error': 'Didnt get email from db correctly. Try again later.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            logger.warning(f"Validation failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        token = request.query_params.get('token')
        try:
            sub = EmailVerify.objects.get(email=email, token=token)
            if sub.verified:
                return Response({'message': 'Email already verified'}, status=status.HTTP_200_OK)
            sub.verified = True
            sub.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except EmailVerify.DoesNotExist:
            return Response({'error': 'Invalid verification link'}, status=status.HTTP_400_BAD_REQUEST)

# @ensure_csrf_cookie
# def get_csrf_token(request):
#     return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})