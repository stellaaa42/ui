import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import Area, Service, CustomUser

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

def load_services():
    """Load predefined services into the database."""
    services_to_create = [
        {"name": "Standard", "price_per_hour": 39},
        {"name": "Premium", "price_per_hour": 50},
        {"name": "Custom", "price_per_hour": 80},
    ]

    for service_data in services_to_create:
        obj, created = Service.objects.get_or_create(name=service_data["name"], defaults={"price_per_hour": service_data["price_per_hour"]})
        if created:
            print(f"✅ Created Service: {obj.name} - ${obj.price_per_hour}")
        else:
            print(f"⚠️ Service Already Exists: {obj.name}")

def load_users():
    test_users = [
        {"username": "testuser1", 
        "password": "testpass123",
        "email": "test1@example.com"},
        {"username": "testuser2", 
        "password": "supersecure456",
        "email": "test2@example.com"},
    ]

    for user_data in test_users:
        username = user_data["username"]
        password = user_data["password"]
        email = user_data["email"]

        user, created = CustomUser.objects.get_or_create(username=username, defaults={"email": email} )
        if created:
            user.set_password(password)  # Set password properly (hashed)
            user.save()
            print(f"✅ Created user: {username} with password: {password}")
        else:
            print(f"⚠️ User {username} already exists!")

    print("🚀 Test users loaded successfully!")

TEST_USER = {
    "username": "testuser1",
    "password": "testpass123"
}

def login_user():
    LOGIN_URL = "http://127.0.0.1:8000/api/auth/login/"
    response = requests.post(LOGIN_URL, json=TEST_USER)

    if response.status_code == 200:
        with open(COOKIE_FILE, "w") as file:
            file.write(response.headers.get("Set-Cookie", ""))
        print("✅ Logged in successfully.")
    else:
        print(f"❌ Login failed: {response.status_code} - {response.text}")

def logout_user():
    LOGOUT_URL = "http://127.0.0.1:8000/api/auth/logout/"
    try:
        with open(COOKIE_FILE, "r") as file:
            cookies = file.read().strip()
        headers = {"Cookie": cookies}
    except FileNotFoundError:
        print("❌ No cookie file found. Login first.")
        return

    response = requests.post(LOGOUT_URL, headers=headers)

    if response.status_code in [200, 205]:
        print("✅ Logged out successfully.")
    else:
        print(f"❌ Logout failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # load_areas()
    # load_services()
    # load_users()
    # login_user()
    logout_user()
