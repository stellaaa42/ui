import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import Area, Item

def load_areas():
    """Load predefined areas into the database."""
    areas_to_create = [
        {"name": "One room", "description": "Small area, 20 sqm"},
        {"name": "Two rooms", "description": "Medium area, 40 sqm"},
        {"name": "Three or More rooms", "description": "Large area, 60 sqm+"},
    ]

    for area_data in areas_to_create:
        obj, created = Area.objects.get_or_create(name=area_data["name"], defaults={"description": area_data["description"]})
        if created:
            print(f"✅ Created: {obj.name}")
        else:
            print(f"⚠️ Already exists: {obj.name}")

    print("\n📌 All areas in the database:")
    for area in Area.objects.all():
        print(f"- {area.name}: {area.description}")

def load_services():
    """Load predefined services (items) into the database."""
    services_to_create = [
        {"name": "Standard", "price_per_hour": 39},
        {"name": "Premium", "price_per_hour": 50},
        {"name": "Custom", "price_per_hour": 80},
    ]

    for service_data in services_to_create:
        obj, created = Item.objects.get_or_create(name=service_data["name"], defaults={"price_per_hour": service_data["price_per_hour"]})
        if created:
            print(f"✅ Created Service: {obj.name} - ${obj.price_per_hour}")
        else:
            print(f"⚠️ Service Already Exists: {obj.name}")

if __name__ == "__main__":
    load_areas()
    load_services()
