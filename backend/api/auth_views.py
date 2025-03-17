from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.views import View

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
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            access_token = AccessToken.for_user(user)
            response = Response({
                "access_token": str(access_token),
                "user": {"name": user.username}
            })
            response.set_cookie("access_token", str(access_token), httponly=True, samesite="Lax")
            return response
            
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out"}, status=205)
        response.delete_cookie("access_token")  # Just removes the cookie
        return response

class UserInfoView(View):
    def get_user_from_session(self, session_key):
        try:
            session = Session.objects.get(
                session_key=session_key,
                expire_date__gte=timezone.now()
            )
            session_data = session.get_decoded()
            user_id = session_data.get('_auth_user_id')
            if not user_id:
                return None

            user = User.objects.get(pk=user_id)
            return {
                'username': user.username,
                'email': user.email,
                # Add any more fields you crave
            }
        except Session.DoesNotExist:
            return None

    def post(self, request):
        session_key = request.POST.get('token')
        print('session key', session_key)
        if not session_key:
            return JsonResponse(
                {'error': 'Session key not provided'}, status=400
            )

        user_data = self.get_user_from_session(session_key)

        if not user_data:
            return JsonResponse({"error": "userinfo auth_view post, invalid or expired session"}, status=401)
        return JsonResponse({'user': user_data}, status=200)