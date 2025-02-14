import stripe
from rest_framework import serializers
from django.conf import settings
from .models import Booking, Item
from datetime import date

# stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    # Allow selection of service
    service = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all()) 
    payment_intent_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'

    # def create(self, validated_data):
        # Create a Stripe Payment Intent (Only Authorize, Not Charge)
        # payment_intent = stripe.PaymentIntent.create(
        #     amount=5000,  # Example: $50.00 (Stripe uses cents)
        #     currency="eur",
        #     payment_method_types=["card"],
        #     capture_method="manual",  # Manual capture ensures no immediate charge
        # )

        # validated_data["payment_intent_id"] = payment_intent["id"]
        # validated_data["payment_status"] = "authorized"

        # return super().create(validated_data)


    def validate_appointment_date(self, value):
        """Ensure the booking date is in the future."""
        if value < date.today():
            raise serializers.ValidationError("Appointment date must be in the future.")
        return value
    
    def validate_card(self, data):
        """Ensure card details are provided if payment method is 'card'"""
        if data.get("payment_method") == "credit_card":
            if not data.get("card_number") or not data.get("card_cvv") or not data.get("card_expiration") or not data.get("billing_address"):
                raise serializers.ValidationError("All card details must be provided for card payments.")
            
            # Validate expiration date format (MM/YYYY)
            if not re.match(r"^(0[1-9]|1[0-2])/\d{4}$", data["card_expiration"]):
                raise serializers.ValidationError({"card_expiration": "Expiration date must be in MM/YYYY format."})

        return data