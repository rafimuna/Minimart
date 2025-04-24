# users/models.py

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# ✅ কাস্টম ম্যানেজার: ইউজার তৈরি ও সুপারইউজার তৈরির জন্য আলাদা ক্লাস
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # ইউজার ইমেইল ছাড়া তৈরি করা যাবে না
        if not email:
            raise ValueError('ইমেইল ঠিকানা অবশ্যই দিতে হবে')

        # ইমেইল ঠিকভাবে সেট করে নিলাম
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # পাসওয়ার্ড হ্যাশ করে সেট করা
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # সুপার ইউজার তৈরির জন্য নিচের ফিল্ড গুলো True হতে হবে
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

# ✅ মেইন ইউজার মডেল
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # ইউজারনেম এর বদলে ইমেইল
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # কোন ফিল্ড দিয়ে login হবে
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # create_superuser এর সময় লাগবে

    objects = CustomUserManager()

    def __str__(self):
        return self.email
