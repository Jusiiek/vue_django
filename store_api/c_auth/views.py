# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils import timezone
from datetime import timedelta
from .models import AuthToken
from .utils import get_token_from_header
from users.models import User


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if not email:
            return Response(
                {'error': 'No email provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(email=email)
        AuthToken.objects.filter(user=user, expires_at__gt=timezone.now()).delete()

        token = AuthToken.objects.create(
            user=user,
            token_type='login',
            expires_at=timezone.now() + timedelta(hours=1)
        )
        return Response({'token': str(token.token)}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token_str = get_token_from_header(request)
        if not token_str:
            return Response(
                {'error': 'No authenticated user found'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            token = AuthToken.objects.get(token=token_str)
            token.delete()
            return Response({'detail': 'Logged out'}, status=status.HTTP_401_UNAUTHORIZED)
        except AuthToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
