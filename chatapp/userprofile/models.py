"""
User Profile Models.
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from base.models import BaseModel
# from authentication.models import User


User = get_user_model()


class UserDetails(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="details",
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=50,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="static/images/profile",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.first_name or self.user.email


class ContactInformation(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact",
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r"^\+?1?\d{9,15}$")],
        blank=True,
    )
    address = models.TextField(blank=True)
    postal_code = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.phone_number
