"""
created at ৯/১০/২১
"""
__author__ = 'Nazmul Hasan Sani'

from core_app.models import ConsoleUser


class DBRouter(object):

    def db_for_read(self, model, **hints):
        if model == ConsoleUser:
            return 'user_db'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model == ConsoleUser:
            return 'user_db'
        else:
            return 'default'
