from rest_framework.request import Request
from .models import AuthToken
from users.models import User


def get_token_from_header(request: Request) -> str or None:
    """
    Extracts the token string from Authorization header.
    Expects format: Authorization: Bearer <token>
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None

    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == 'bearer':
        return parts[1]
    return None


def get_user_by_token(token_str: str) -> User or None:
    """
    Returns the user associated with the token if valid and not expired.
    """
    if not token_str:
        return None

    try:
        token = AuthToken.objects.get(token=token_str)
        if token.is_expired():
            return None
        return token.user
    except AuthToken.DoesNotExist:
        return None


def get_authenticated_user(request: Request) -> User or None:
    """
    Returns an authenticated user if valid and not expired.
    """
    token = get_token_from_header(request)
    if not token:
        return None
    user = get_user_by_token(token)
    return user if user else None
