from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid



class AccountManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = Account(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("last_name", "Clinic")
        extra_fields.setdefault("first_name", "Administrator")

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):
    username = None  
    email = models.EmailField(unique=True)
    otp = models.IntegerField(null=True)
    verified = models.BooleanField(default=False)
    birthday = models.IntegerField(null=True)

    gender = models.CharField(choices=(('Male','Male'), ('Female', 'Female')), max_length=10)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    specialization = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True)
    user_type = models.CharField(choices=(('Doctor','Doctor'), ('Staff', 'Staff'), ('Patient', 'Patient')), max_length=10)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = AccountManager()

    def qrcode_url(self):
        if self.qr_code and hasattr(self.qr_code, 'url'):
            return self.qr_code.url
        else:
            return "/static/sb_admin/img/user.png"

    def __str__(self):
        return self.last_name + " " + self.first_name

