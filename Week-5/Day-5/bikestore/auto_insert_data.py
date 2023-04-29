import os
import django
import random
import datetime
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore.settings')
django.setup()

from rent.models import Customer, Vehicle, Rental
fake = Faker()


def get_random_datetime(): #between start_date and now
    start_date = datetime.datetime(2022, 1, 1, 0, 0, 0) 
    now = datetime.datetime.now()
    time_between_dates = now - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    # дает рандомные дату и время в диапазоне между старт дейт и сейчас
    random_datetime = random_date.replace(hour=random.randint(0, 23),
        minute=random.randint(0, 59), second=random.randint(0, 59)).strftime('%Y-%m-%d %H:%M:%S')
    # преобразует рандомную дату из стринга в датетайм формат
    random_datetime = datetime.datetime.strptime(random_datetime, '%Y-%m-%d %H:%M:%S')
    return random_datetime




def create_customers():
    ISRAELI_CITIES = ['Tel Aviv', 'Haifa', 'Jerusalem', 'Rishon LeZion', 'Petah Tikva', 'Ramat Gan', 'Holon', 'Givatayim', 'Bat Yam People Republic']
    for i in range(1):
        isrcity = random.choice(ISRAELI_CITIES)
        email = fake.email()
        phnumber = '05' + str(round((random.uniform(0.1, 1)*100000000))-1)
        # Check if email or phone number already exists in database
        if Customer.objects.filter(email=email).exists() or Customer.objects.filter(phone_number=phnumber).exists():
            print(f"{i+1}'st iteration user with email {email} or phone number {phnumber} already exists and thus doesn't added.")
            return None
        else:
            Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                phone_number=phnumber,
                address=fake.street_address(),
                city=isrcity,
                country="IL"
                )   
            customer = Customer.objects.filter(phone_number=phnumber)
            customer = customer.first()
            # customer_id = Customer.objects.filter(phone_number=phnumber).values()[0]['id']
            # print(f"{i+1}'st iteration user (phone: {phnumber}) added successfully with id: {customer_id}")
            return customer

# vehicle_type_names = [vt.name for vt in Vehicle_Type.objects.all()]
# random_vehicle = random.choice(vehicle_type_names)
# random_vehicle_type_id = Vehicle.objects.filter(name=random_vehicle).values()[0]['id']


def add_rental_record():

    rand_rental_date = get_random_datetime()
    #with some probability gives None or return date that newest than rental date and oldest than now
    for i in range(3):
        rand_return_date = get_random_datetime()
        if rand_rental_date < rand_return_date:
            break
        else:
            rand_return_date = None
    # vehicle_ids_list = list(Vehicle.objects.values_list('id', flat=True))
    # random_vehicle_id = random.choice(vehicle_ids_list)

    rand_customer = create_customers()
    while not rand_customer:
        rand_customer = create_customers()

    random_vehicle = random.choice(Vehicle.objects.all())

    Rental.objects.create(
                rental_date=rand_rental_date,
                return_date=rand_return_date,
                customer_id=rand_customer,
                vehicle=random_vehicle
                )   
    new_rent = Rental.objects.filter(
                rental_date=rand_rental_date,
                return_date=rand_return_date,
                customer_id=rand_customer,
                vehicle=random_vehicle)
    print(f"New rental record has been added successfully:\n{new_rent}\n")
    # print(f"New user has been added successfully: {rand_customer}")



if __name__ == '__main__':
    for i in range(3):
        add_rental_record()


