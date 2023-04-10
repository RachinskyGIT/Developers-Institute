# # ex1
# class MathPrint:
#     """
# The programm (implemented as a class) can can take a numeric value 
# both from input and as code, change this value using several mathematical operations, 
# and print the resulting value to the screen.
# """
    
#     def __init__(self, number=None):
#         self.number = number

#     def inp(self):
#         self.number = (input('enter the new value: '))

#     def disp(self):  
#         print(self.number)

#     def __int__(self):
#         try:
#             self.number = int(self.number)
#         except ValueError:
#             print("Your value is not a value")
        
#     def __abs__(self):
#         if (type(self.number)==(int or float)) and (self.number < 0):
#                 self.number *= -1 

# # aue = MathPrint(-5)
# # aue.__int__()
# # aue.__abs__()
# # aue.inp()
# # aue.disp()
# # print(MathPrint.__doc__)
# # aue.displayObject()


# # https://mathspp.com/blog/pydonts/dunder-methods#:~:text=In%20Python%2C%20dunder%20methods%20are,__%20or%20__add__%20.
# # class DictSubclass(dict):
# #     def __missing__(self, key):
# #         print(f"Missing {key = }")

# # my_dict = DictSubclass()
# # my_dict[0] = True
# # if my_dict[0]:
# #     print("Key 0 was `True`.")
# # # Prints: Key 0 was `True`
# # my_dict[1]  # Prints: Missing key = 1


# # ex2

# class Currency:  
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __add__(self, other):
#         if type(other)==int:
#             return self.amount+other
#         if self.currency==other.currency:
#             return self.amount + other.amount
#         else:
#             raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")
    
#     def __iadd__(self, other):
#         if type(other)==int:
#             self.amount+=other
#             return self
#         if self.currency.lower()==other.currency.lower():
#             self.amount += other.amount
#             return self
#         else:
#             raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")    

#     def __str__(self):
#         return f"'{self.amount} { self.currency}s'"

#     def __repr__(self):
#         return f"'{self.amount} { self.currency}s'"

    
#     def __int__(self):
#         return self.amount

# deng=Currency("Dollar",5)
# cesef=Currency("dollar",7)

# deng+=cesef
# print (deng)

    


# # Exercises XP+ Modules

# # ex1
# from func import funcc as func_add
# func_add(1,6)
# func.funcc(1,1)

# # ex2
# import func
# func.random_game(1)

# # ex3
# def sendyourcode():
#     import random 
#     import string
#     code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))    
#     print(code)

# sendyourcode()

# # # ex5
# def howmanydays():
#     import datetime
#     today = datetime.datetime.now()
#     print(f"{(datetime.datetime(today.year+1, 1, 1) - today).days} days remaining until next 1st January")

# howmanydays()

# # ex6
# def bdminutes():
#     from datetime import datetime
#     birthday = input("Enter your date of birth (dd.mm.yyyy): ")
#     bday = datetime.strptime(birthday, '%d.%m.%Y')
#     today = datetime.now()
#     seconds = ((today-bday).days*24*60*60)+(today-bday).seconds
#     print(f"Approximately '{'{0:,}'.format(seconds)}' seconds you lived until now. Enjoy.")

# bdminutes()

# # ex8
# def jupiter():
#     from datetime import datetime
#     birthday = input("Enter your date of birth (dd.mm.yyyy): ")
#     bday = datetime.strptime(birthday, '%d.%m.%Y')
#     today = datetime.now()
#     age = (((today-bday).days*24*60*60)+(today-bday).seconds)/(365*24*60*60)
#     print(f"Your age on the following planets will be:\n\
#     Earth: {round(age)} years\n\
#     Mercury: {round(age/0.2408467)} years\n\
#     Venus: {round(age/0.61519726)} years\n\
#     Mars: {round(age/1.8808158)} years\n\
#     Jupiter: {round(age/11.862615)} years\n\
#     Saturn: {round(age/29.447498)} years\n\
#     Uranus: {round(age/84.016846)} years\n\
#     Neptune: {round(age/164.79132)} years")

# jupiter()


# ex9
def input_fake_user_data(x, users = []): 
    from faker import Faker 
    from random import randint   
    fake = Faker('en_US') 

    user_data = {}
    for i in range(0, x): 
        user_data[i]={} 
        user_data[i]['id']= '{0:,}'.format(randint(1, 999999999)).replace(',', ' ')
        user_data[i]['name']= ''.join(' ' + char if char.isupper() else char.strip() for char in fake.color_name()).strip()
        user_data[i]['address']= fake.address() 
        user_data[i]['language_code']= fake.language_code().upper()
        user_data[i]['MAC Address']= fake.hexify(text='^^:^^:^^:^^:^^:^^', upper=True)
        users.append(user_data[i])
    return users

def print_fake_user_data(users): 
    for j in users:
            print("{\n" + "\n".join("{!r}: {!r}".format(k, v) for k, v in j.items()) + "\n}")
  
fakeusers = input_fake_user_data(2)
print_fake_user_data(fakeusers)



