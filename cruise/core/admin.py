from django.contrib import admin
from .models import UserModule, Admin, Employee, Customer, Cruise, Booking, Payment, OnboardService, Task, Inventory, Promotion, CustomerBooking

admin.site.register(UserModule)
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Cruise)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(OnboardService)
admin.site.register(Task)
admin.site.register(Inventory)
admin.site.register(Promotion)
admin.site.register(CustomerBooking)

