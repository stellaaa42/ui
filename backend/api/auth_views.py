from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

User = get_user_model()

class SignupView(APIView):
    permission_classes = [AllowAny]  # Because, duh, new users need access

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=400)

        user = User.objects.create(username=username, password=make_password(password))
        return Response({"message": "Signup successful, now go login."}, status=201)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            response = Response({
                "access": str(refresh.access_token),
                "user": {"name": user.username}
            })
            response.set_cookie("refresh_token", str(refresh), httponly=True, samesite="Lax")
            return response
        return Response({"error": "Invalid credentials"}, status=400)

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token missing"}, status=403)

        try:
            refresh = RefreshToken(refresh_token)
            return Response({"access": str(refresh.access_token)})
        except Exception:
            return Response({"error": "Invalid refresh token"}, status=403)

class LogoutView(APIView):
    def post(self, request):
        response = JsonResponse({"message": "Logged out"})
        response.delete_cookie("refresh_token")
        return response
