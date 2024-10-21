from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    permissions = models.ManyToManyField('auth.Permission')

    def __str__(self):
        return self.role_name

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity by {self.user.username} on {self.timestamp}"

class Cruise(models.Model):
    cruise_name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cruise_name

class Cabin(models.Model):
    cabin_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cabin_type} - {self.cruise.cruise_name}"

class Fleet(models.Model):
    ship_name = models.CharField(max_length=255)
    maintenance_schedule = models.DateField()

    def __str__(self):
        return self.ship_name
