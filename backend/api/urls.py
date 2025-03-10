from django.urls import path, include
from .views import (
    ServiceListView, AreaListView, BookingCreateView, BookingListView, get_csrf_token,
)
from .auth_views import (
    SignupView, LoginView, LogoutView, RefreshTokenView
)

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('bookings/create', BookingCreateView.as_view(), name='book-create'),
    path('bookings/', BookingListView.as_view(), name='bookings-list'),

    path('csrf/', get_csrf_token),

    path("auth/", include([
            path("signup/", SignupView.as_view(), name="signup"),
            path("login/", LoginView.as_view(), name="login"),
            path("logout/", LogoutView.as_view(), name="logout"),
            path("refresh/", RefreshTokenView.as_view(), name="refresh-token"),
            path('oauth/', include('allauth.socialaccount.urls')),
        ])),
]