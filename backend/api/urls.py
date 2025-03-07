from django.urls import path, include
from .views import (
    ItemListView, AreaListView, BookingCreateView, UserBookingListView, get_csrf_token,
)
from .auth_views import (
    SignupView, LoginView, LogoutView, RefreshTokenView
)

urlpatterns = [
    path('items/', ItemListView.as_view(), name='service-list'),
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('book/', BookingCreateView.as_view(), name='book-service'),  # ✅ Anyone can create a booking (POST only)
    path('my-bookings/', UserBookingListView.as_view(), name='my-bookings'),

    path('csrf/', get_csrf_token),

    path("auth/", include([
            path("signup/", SignupView.as_view(), name="signup"),
            path("login/", LoginView.as_view(), name="login"),
            path("logout/", LogoutView.as_view(), name="logout"),
            path("refresh/", RefreshTokenView.as_view(), name="refresh-token"),
            path('oauth/', include('allauth.socialaccount.urls')),
        ])),
]