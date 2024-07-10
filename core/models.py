from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    # id = models.UUIDField(name="id", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(name="created_at", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(name="updated_at", auto_now=True)

    class Meta:
        abstract = True


class Account(AbstractUser):

    email = models.EmailField(name="email", max_length=100, unique=True,
                              blank=False, null=False, editable=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username', 'password', 'first_name',)

    def __str__(self) -> str:
        return f"{self.email}"


class Metadata(models.Model):
    name = models.CharField(name="name", editable=True, null=False, blank=False, max_length=64)

    author = models.ForeignKey(
        to="Account",
        # author == User
        related_name="metadata",
        name="author",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )


class Registry(Base):
    name = models.CharField(name="name", editable=True, null=False, blank=False, max_length=64)

    metadata = models.OneToOneField(
        to="Metadata",
        related_name="registry",
        name="metadata",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

