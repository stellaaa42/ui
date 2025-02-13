from django.db import models
from django.contrib.auth.models import User
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # in minutes

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    payment_status = models.BooleanField(default=False)

@csrf_exempt  # Disable CSRF for simplicity (ensure security in production)
def create_checkout_session(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            service_id = data.get("service_id")
            service = Service.objects.get(id=service_id)
            
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': service.name,
                        },
                        'unit_amount': int(service.price * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:5173/success',
                cancel_url='http://localhost:5173/cancel',
            )
            return JsonResponse({'id': session.id})
        except Service.DoesNotExist:
            return JsonResponse({'error': 'Service not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
