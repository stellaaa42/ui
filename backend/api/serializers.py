import stripe
from rest_framework import serializers
from django.conf import settings
from .models import Booking, Service, Area, EmailVerify
from datetime import date, datetime
import re


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all()) 
    # payment_intent_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_appointment_date(self, value):
        """Ensure the booking date is in the future."""
        if value < date.today():
            raise serializers.ValidationError("Appointment date must be in the future.")
        return value
    
    def validate(self, data):
        if data.get("payment_method") in ("credit_card", "debit_card"):
            required_fields = ["card_number", "card_cvv", "card_expiration", "billing_address"]
            missing_fields = {field: "This field is required." for field in required_fields if not data.get(field)}

            if missing_fields:
                raise serializers.ValidationError(missing_fields)

            # Validate expiration date format & check if expired
            if not re.fullmatch(r"(0[1-9]|1[0-2])/\d{4}", data["card_expiration"]):
                raise serializers.ValidationError({"card_expiration": "Use MM/YYYY format."})

            exp_month, exp_year = map(int, data["card_expiration"].split("/"))
            if datetime(exp_year, exp_month, 1) < datetime.today().replace(day=1):
                raise serializers.ValidationError({"card_expiration": "Card is expired."})

        return data
    
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

class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerify
        fields = '__all__'

# stripe.api_key = settings.STRIPE_SECRET_KEY