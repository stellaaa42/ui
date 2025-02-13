from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2, default=35.00)

    def __str__(self):
        return f"{self.name} - €{self.price_per_hour}/hour"

class Booking(models.Model):

    AREA_CHOICES = [
        ('one_bedroom', 'One Bedroom (20 sqm)'),
        ('two_bedroom', 'Two Bedrooms (40 sqm)'),
        ('three_plus_bedroom', 'Three or More Bedrooms (60 sqm)'),
    ]

    PAYMENT_CHOICES = [
            ('card', 'Credit/Debit Card'),
            ('paypal', 'PayPal'),
        ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    service = models.ForeignKey(Item, on_delete=models.CASCADE)
    area = models.CharField(max_length=20, choices=AREA_CHOICES) 

    # Stripe Payment Intent ID
    payment_intent_id = models.CharField(max_length=255, blank=True, null=True)  
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_cvv = models.CharField(max_length=3, blank=True, null=True)  # Optional
    card_expiration = models.DateField(max_length=7, blank=True, null=True)  # Format: MM/YYYY
    billing_address = models.TextField(blank=True, null=True)  # Optional


    def __str__(self):
        return f"Booking by {self.name}, {self.email}, {self.phone} on {self.appointment_date} at {self.appointment_time}, {self.message}, {self.created_at}"

