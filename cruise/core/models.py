from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

class UserModule(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        related_name='user_module_set',
        blank=True,
        help_text="Groups this user belongs to."
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_module_permissions_set',
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return self.email

class Admin(models.Model):
    user = models.OneToOneField(UserModule, on_delete=models.CASCADE, related_name='admin_profile')
    managed_cruises = models.ManyToManyField('Cruise', related_name='managed_by_admin')

    def __str__(self):
        return f"Admin: {self.user.username}"

class Employee(models.Model):
    user = models.OneToOneField(UserModule, on_delete=models.CASCADE, related_name='employee_profile')
    position = models.CharField(max_length=100)
    tasks = models.ManyToManyField('Task', related_name='employees')
    
    def __str__(self):
        return f"Employee: {self.user.username}"

class Customer(models.Model):
    user = models.OneToOneField(UserModule, on_delete=models.CASCADE, related_name='customer_profile')
    loyalty_points = models.IntegerField(default=0)
    bookings = models.ManyToManyField('Booking', through='CustomerBooking', related_name='customer_bookings')

    def __str__(self):
        return f"Customer: {self.user.username}"

class Cruise(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    cabins_available = models.IntegerField()

    def __str__(self):
        return f"Cruise: {self.name} to {self.destination}"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    cabin_number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_bookings')

    def __str__(self):
        return f"Booking: {self.cruise.name} by {self.customer.user.username}"
    
class CustomerBooking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for {self.booking.cruise.name}, Amount: {self.amount}"

class OnboardService(models.Model):
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='onboard_services')
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50)  # Meal, Activity, etc.
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Service: {self.service_name} on {self.cruise.name}"

class Task(models.Model):
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.description}, Due: {self.due_date}"

class Inventory(models.Model):
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='inventory')
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Inventory: {self.item_name} on {self.cruise.name}"

class Promotion(models.Model):
    title = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Promotion: {self.title}, {self.discount_percentage}% off"

