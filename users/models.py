from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('O email é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom User model that uses email as the unique identifier
    instead of username for authentication.
    """
    
    # Remove username field
    username = None
    
    # Email as the unique identifier
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        error_messages={
            'unique': 'Um usuário com este email já existe.',
        },
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        verbose_name='criado em',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='atualizado em',
        auto_now=True,
    )
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # Use custom manager
    objects = UserManager()
    
    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email
