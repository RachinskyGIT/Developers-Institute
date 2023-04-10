# ex1
class MathPrint:
    """
The programm (implemented as a class) can can take a numeric value 
both from input and as code, change this value using several mathematical operations, 
and print the resulting value to the screen.
"""
    
    def __init__(self, number=None):
        self.number = number

    def inp(self):
        self.number = (input('enter the new value: '))

    def disp(self):  
        print(self.number)

    def __int__(self):
        try:
            self.number = int(self.number)
        except ValueError:
            print("Your value is not a value")
        
    def __abs__(self):
        if (type(self.number)==(int or float)) and (self.number < 0):
                self.number *= -1 

# aue = MathPrint(-5)
# aue.__int__()
# aue.__abs__()
# aue.inp()
# aue.disp()
# print(MathPrint.__doc__)
# aue.displayObject()


# https://mathspp.com/blog/pydonts/dunder-methods#:~:text=In%20Python%2C%20dunder%20methods%20are,__%20or%20__add__%20.
# class DictSubclass(dict):
#     def __missing__(self, key):
#         print(f"Missing {key = }")

# my_dict = DictSubclass()
# my_dict[0] = True
# if my_dict[0]:
#     print("Key 0 was `True`.")
# # Prints: Key 0 was `True`
# my_dict[1]  # Prints: Missing key = 1


# ex2

class Currency:  
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        if type(other)==int:
            return self.amount+other
        if self.currency==other.currency:
            return self.amount + other.amount
        else:
            raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")
    
    def __iadd__(self, other):
        if type(other)==int:
            self.amount+=other
            return self
        if self.currency==other.currency:
            self.amount += other.amount
            return self
        else:
            raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")    

    def __str__(self):
        return f"'{self.amount} { self.currency}s'"

    def __repr__(self):
        return f"'{self.amount} { self.currency}s'"

    
    def __int__(self):
        return self.amount

deng=Currency("Dollar",5)
cesef=Currency("Dollar",7)

deng+=cesef
print (deng)

    