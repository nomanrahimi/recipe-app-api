"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ django command to wait database. """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write('Database is unavailable wait for 1 sec')
                time.sleep(1)
            self.stdout.write(self.style.SUCCESS('Database is Avaiable'))
