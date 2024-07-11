from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from core.models import Account, Registry, Metadata
import os
import subprocess


class Command(BaseCommand):
    help = "seed database"

    @staticmethod
    def delete_db():
        if os.path.isfile("./db.sqlite3"):
            os.remove("./db.sqlite3")

    @staticmethod
    def delete_migration():
        if os.path.isfile("./core/migrations/0001_initial.py"):
            os.remove("./core/migrations/0001_initial.py")

    @staticmethod
    def migrate():
        subprocess.run(['python', 'manage.py', 'makemigrations'])
        subprocess.run(['python', 'manage.py', 'migrate'])

    def handle(self, *args, **options):
        self.delete_db()
        self.delete_migration()
        self.migrate()

        faker = Faker()

        account = Account.objects.create(
            username=faker.user_name(),
            password=make_password("123"),
            email=faker.email(),
            is_superuser=False,
            is_staff=False,
            is_active=True
        )