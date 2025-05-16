from django.db import models
from django.utils import timezone
import uuid

from users.models import User

# Create your models here.

class AuthToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth_tokens')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def __str__(self):
        return f'Token for {self.user.email}'
