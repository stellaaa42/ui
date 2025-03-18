from django.urls import path, include
from .views import (
    ServiceListView, AreaListView, BookingCreateView, 
    BookingListView,
)
from .auth_views import (
    SignupView, LogoutView, UserInfoView, LoginView,
    RefreshTokenView,
)

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('bookings/create', BookingCreateView.as_view(), name='book-create'),
    path('bookings/', BookingListView.as_view(), name='bookings-list'),

    path("auth/", include([
            path("signup/", SignupView.as_view(), name="signup"),
            path('login/', LoginView.as_view(), name='login'),
            path('api/auth/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
            path('oauth/', include('allauth.socialaccount.urls')),
            path("logout/", LogoutView.as_view(), name="logout"),
            path('user-info/', UserInfoView.as_view(), name='user_info'),

        ])),
]