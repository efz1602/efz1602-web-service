from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from ews_api.contacts.settings import STUDENT_NUMBER_MIN, STUDENT_NUMBER_MAX

User = get_user_model()


# Create your models here.


class Contact(models.Model):
    student_number = models.IntegerField(primary_key=True,
                                         validators=[
                                             # TODO: refactor these out to settings
                                             MinValueValidator(STUDENT_NUMBER_MIN),
                                             MaxValueValidator(STUDENT_NUMBER_MAX),
                                         ])
    name = models.CharField(max_length=10)
    primary_phone = PhoneNumberField(blank=True, null=True)
    secondary_phone = PhoneNumberField(blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    field_or_industry = models.CharField(max_length=50, blank=True, null=True)
    school_or_company = models.CharField(max_length=50, blank=True, null=True)
    degree_or_job = models.CharField(max_length=50, blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['student_number']
