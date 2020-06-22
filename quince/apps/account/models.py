from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        verbose_name="Электронная почта"
    )
    username = models.CharField("Имя пользователя", max_length=50, unique=True)
    biography = models.TextField("Биография", max_length=1000, blank=True)
    is_active = models.BooleanField("Подтвержденный аккаунт", default=True)
    is_private = models.BooleanField("Приватный аккаунт", default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    USERNAME_FIELD = 'email'

    # objects = UserManager()

    def __str__(self):
        return self.email


class ProxyUser(User):
    pass

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ProxyToken(Token):
    pass

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

