from django.contrib import admin
from .models import Customer, Vehicle_Type, Vehicle_Size, Vehicle, Rental,Rental_Rate


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'date_created', 'real_cost', 'size')

class Vehicle_TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Vehicle_SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RentalAdmin(admin.ModelAdmin):
    list_display = ('rental_date', 'return_date', 'customer_id', 'vehicle')

class Rental_RateAdmin(admin.ModelAdmin):
    list_display = ('daily_rate', 'vehicle_type', 'vehicle_size')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Vehicle_Type, Vehicle_TypeAdmin)
admin.site.register(Vehicle_Size, Vehicle_SizeAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(Rental_Rate, Rental_RateAdmin)

