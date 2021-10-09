"""
created at ৯/১০/২১
"""
from django.db import models

__author__ = 'Nazmul Hasan Sani'


class Measurement(models.Model):
    user_id = models.SmallIntegerField(default=None)
    weight = models.SmallIntegerField(help_text='Weight')
    height = models.SmallIntegerField(help_text='Height')
    width = models.SmallIntegerField(help_text='Width')
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'core_app'
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'

    def __str__(self):
        from core_app.models import ConsoleUser
        user = ConsoleUser.objects.filter(id=self.user_id).last()
        return f'{user.name}' if user else f'{self.user_id}'
