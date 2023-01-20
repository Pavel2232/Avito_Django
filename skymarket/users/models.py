from enum import Enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager


class UserRoles(models.TextChoices):
    USER = 'user','User'
    ADMIN = 'admin','Admin'

class User(AbstractBaseUser):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255,unique=True)
    role = models.CharField(max_length=5,choices=UserRoles.choices)
    image = models.ImageField(upload_to='django_media/',null=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin



    objects = UserManager()

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту



    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email