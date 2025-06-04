import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "global_admin@test.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass")

if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create_superuser(
        email=email,
        password=password
    )
else:
    print("Superuser already exists.")
