"""
created at ৯/১০/২১
"""
from django.db import models
from django_cryptography.fields import encrypt

__author__ = 'Nazmul Hasan Sani'


class ConsoleUser(models.Model):
    name = encrypt(models.CharField(max_length=100, help_text='User name'))
    email = encrypt(models.EmailField(help_text='User email'))
    street = encrypt(models.CharField(default=None, max_length=200, help_text='Street'))
    street_2 = encrypt(models.CharField(default=None, max_length=200, help_text='Street 2'))
    city = encrypt(models.CharField(default=None, help_text='City', max_length=150))
    country = encrypt(models.CharField(max_length=150))

    class Meta:
        app_label = 'core_app'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name
