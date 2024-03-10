from django.db import models

from website.utils import generate_uuid


class Employee(models.Model):
    # New feature in Django 5.0
    Departments = models.TextChoices("Departments", "IT HR Finance")

    uuid = models.CharField(
        max_length=100, editable=False, primary_key=True, default=generate_uuid
    )
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(
        max_length=20, choices=Departments, default=Departments.IT
    )
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, editable=False)

    def __str__(self):
        return self.fullname
