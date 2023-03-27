import binascii
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

class MyAccountManager(BaseUserManager):
    """defines the methods to manage the custom user to be created
    Args:
        BaseUserManager ([type]): [description]
    Returns:
        [type]: [description]
    """
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have and email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    """This will define the custom user model to be used
    Args:
        AbstractBaseUser ([type]): [description]
    """
    email = models.EmailField(verbose_name="email",max_length=100,unique=True,null=True)
    username = models.CharField(max_length=30,unique=True)
    company = models.TextField(null=True)
    employee_id = models.CharField(max_length=16,null=True)
    admin = models.IntegerField(null=True)
    server_code = models.CharField(max_length=10,null=True)
    confirm_start_shift = models.BooleanField(default=False) 
    on_shift = models.BooleanField(default=False)
    confirm_end_shift = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def delete_user(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(
        Account,
        null=True,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    def __str__(self):
        return  f"{self.user.username}'s profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)