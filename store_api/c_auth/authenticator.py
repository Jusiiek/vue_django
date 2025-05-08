from rest_framework.authentication import BaseAuthentication
from .utils import get_authenticated_user


class BearerTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = get_authenticated_user(request)
        if user is not None:
            return (user, None)
        return None
