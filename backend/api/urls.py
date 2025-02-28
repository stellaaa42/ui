from django.urls import path
from .views import BookingCreateView, ItemListView, AreaListView, get_csrf_token
from .auth_views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='service-list'),
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('book/', BookingCreateView.as_view(), name='book-service'),
    path('csrf/', get_csrf_token),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]