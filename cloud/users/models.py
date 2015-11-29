from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    email = models.EmailField('Email Address', max_length=255, unique=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    
    def get_full_name(self):
	return self.email
    
    
    def get_short_name():
	return self.email

    def __unicode__(self):
	return  self.email + "  id:" + str(self.id)

