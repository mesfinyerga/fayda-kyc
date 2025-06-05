from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from typing import Any

class Organization(models.Model):
    """
    Represents a client organization/tenant.
    """
    name = models.CharField(max_length=255, unique=True)
    settings = models.JSONField(default=dict, blank=True)
    branding = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str = None, **extra_fields: Any) -> 'User':
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> 'User':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with organization, role, and status.
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('verifier', 'Verifier'),
        ('viewer', 'Viewer'),
    ]
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'organization', 'role']

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email} ({self.organization})" 