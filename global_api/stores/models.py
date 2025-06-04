from django.db import models

from users.models import User

# Create your models here.

class Store(models.Model):
    domain = models.CharField(editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_api')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
