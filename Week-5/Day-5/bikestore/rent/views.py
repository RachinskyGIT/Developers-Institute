from django.shortcuts import render, get_object_or_404
from .models import Customer, Vehicle_Type, Vehicle_Size, Vehicle, Rental,Rental_Rate
from .forms import CustomerForm
from django.db.models import Q


def All_rentals(request): 
    rentalsNone = Rental.objects.filter(Q(return_date__isnull=True)).order_by('rental_date')
    rentals = Rental.objects.filter(Q(return_date__isnull=False)).order_by('rental_date')
    context = {'rentals': rentals, 'rentalsNone':rentalsNone}
    return render(request, 'rental.html', context)

def Rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    customer = get_object_or_404(Customer, pk=pk)
    context = {'rental': rental, 'customer': customer}
    return render(request, 'rental_detail.html', context)

def Customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'customer_detail.html', context)

def All_customers(request): 
    customers = Customer.objects.order_by('last_name')
    context = {'customers': customers}
    return render(request, 'customer.html', context)

def Vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    rentals = Rental.objects.filter(vehicle=vehicle)
    context = {'vehicle': vehicle, 'rentals': rentals}
    return render(request, 'vehicle_detail.html', context)

def All_vehicles(request): 
    vehicles = Vehicle.objects.select_related('vehicle_type').order_by('vehicle_type__name')
    types = Vehicle_Type.objects.all()
    context = {'vehicles': vehicles, 'types': types}
    return render(request, 'vehicle.html', context)