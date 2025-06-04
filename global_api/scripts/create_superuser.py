import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "global_admin@test.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass")

if not User.objects.filter(email=email).exists():
    print("Creating superuser...")
    User.objects.create_superuser(
        email=email,
        password=password
    )
else:
    print("Superuser already exists.")

print("Checking superuser...")
user = User.objects.filter(email=email).first()
if user:
    print(f"User created successfully: {user}.")
else:
    print("User was not created.")
