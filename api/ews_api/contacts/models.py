from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from ews_api.users.models import User


# Create your models here.


class Contact(models.Model):
    student_number = models.IntegerField(primary_key=True,
                                         validators=[
                                             # TODO: refactor these out to settings
                                             MinValueValidator(20160200),
                                             MaxValueValidator(20160242),
                                         ])
    name = models.CharField(max_length=10)
    primary_phone = PhoneNumberField(blank=True)
    secondary_phone = PhoneNumberField(blank=True)
    city = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=10, blank=True)
    field_or_industry = models.CharField(max_length=50, blank=True)
    school_or_company = models.CharField(max_length=50, blank=True)
    degree_or_job = models.CharField(max_length=50, blank=True)
    other_info = models.TextField(blank=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['student_number']
