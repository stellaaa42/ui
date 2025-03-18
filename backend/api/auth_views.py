from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView

User = get_user_model()

class SignupView(APIView):
    permission_classes = [AllowAny]

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
    def set_jwt_tokens(self, response, access_token, refresh_token):
        response.set_cookie(
            key="access_token",
            value=str(access_token),
            httponly=True,  # Prevent JavaScript access (XSS protection)
            secure=True,  # Set to True in production (HTTPS only)
            samesite="Lax",  # Prevent CSRF attacks while allowing same-site requests
            max_age=900,  # 15 minutes (adjust based on your token lifetime)
        )
        response.set_cookie(
            key="refresh_token",
            value=str(refresh_token),
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=604800,  # 7 days (adjust based on your refresh token lifetime)
        )
        return response
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            response = Response({
                "message": "Login successful", 
                "user": {"name": user.username},
                "access_token": str(access_token),
                "refresh": str(refresh),
                }, status=status.HTTP_200_OK)

            print(response, 'user', user, 'access', access_token, 'refresh', refresh)
            return self.set_jwt_tokens(response, access_token, refresh)  # Set cookies

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")  # Read token from cookie
        if not refresh_token:
            return Response({"error": "Refresh token missing"}, status=status.HTTP_400_BAD_REQUEST)

        request.data["refresh"] = refresh_token  # Inject into request body
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data["access"]
            response = Response({"message": "Token refreshed"}, status=status.HTTP_200_OK)
            response.set_cookie(
                key="access_token",
                value=str(access_token),
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=900,  # 15 min
            )
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out"}, status=205)
        response.delete_cookie("access_token")  # Just removes the cookie
        return response

class UserInfoView(APIView):
    # authentication_classes = [JWTAuthentication]  # ✅ Enforces JWT authentication
    # permission_classes = [IsAuthenticated]  # ✅ Requires authentication

    def get(self, request):
        print(f"🔍 DEBUG: Request Headers: {request.headers}")
        print(f"🔍 DEBUG: Cookies: {request.COOKIES}")
        token = request.COOKIES.get("access_token")
        print(f"🔍 DEBUG: Access Token from Cookies: {token}")
        try:
            # user = request.user 
            # print(f"🔍 DEBUG: Authenticated User: {user}")
            # if not user or user.is_anonymous:
            #     raise AuthenticationFailed("User not authenticated")

            validated_token = AccessToken(token)  # ✅ Decode token manually
            user_id = validated_token["user_id"]  # ✅ Extract user ID from token

            # ✅ Fetch user from DB
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.get(id=user_id)

            print(f"🔍 DEBUG: Authenticated User: {user}")
            return Response({
                "authenticated": True,
                "user": {
                    "id": user.id, 
                    "name": user.username, 
                    "email": user.email
                }
            })  # ✅ DRF handles JSON response automatically

        except Exception as e:
            return Response({"error": "Invalid or expired token", "details": str(e)}, status=401)
