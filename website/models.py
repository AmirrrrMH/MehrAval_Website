from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=50)
    current_field = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    grade = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(20.00)],
    )
    current_school = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    home_phone_number = models.CharField(max_length=20)
    dad_phone_number = models.CharField(max_length=20)
    mom_phone_number = models.CharField(max_length=20)
    student_phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    reason_for_changing_the_school = models.CharField(
        max_length=255, null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Success(models.Model):
    FIELD_CHOICES = [
        ("math", "ریاضی"),
        ("experimental", "تجربی"),
        ("humanities", "انسانی"),
        ("art", "هنر"),
    ]

    student_name = models.CharField(max_length=100)
    field = models.CharField(max_length=20, choices=FIELD_CHOICES)
    image = models.ImageField(upload_to="successes/")
    rank = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.student_name
