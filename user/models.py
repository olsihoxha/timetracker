from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, birthdate, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.birthdate = birthdate
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, birthdate):
        user = self.create_user(
            email,
            password=password,
            birthdate=birthdate
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, birthdate):
        user = self.create_user(
            email,
            password=password,
            birthdate=birthdate
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)  # this could be False if we want to verify by email
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    REQUIRED_FIELDS = ["birthdate"] # this is to create user from cmd with birthdate included

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


