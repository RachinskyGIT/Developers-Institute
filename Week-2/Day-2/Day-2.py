# ex1

my = {1,2,3,4}
another = {5,10}
my.update(another)
friend = {4,5,6,7}
our = my.union(friend)

# # ex2
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


# ex3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0], basket[2]
basket.insert(0, "Apples")
basket.insert(4, "Kiwi")
print(basket)
print(basket.count("Apples"))
basket = basket*0
print(basket)
print ("\n")


# ex4

# 1. It is obvious
# 2. from random import random \ seq=[] \ for i in range(0, 999): seq.append(random()) \ something like this
# 3.
floatlist = []
for i in  range(15, 55, 5 ):
    floatlist.append(i/10)
print (floatlist)
print ("\n")

#ex5

for i in range(0, 21):
    print (i,end=" ")
print ("\n")

for i in range(0, 21):
    if (i%2)==0:
        print (i,end=" ")
print ("\n")
        

# ex6

active = True
while active:
    print("Write the right name")
    inpname = input("Right name is: ")
    if inpname == "Name":
        active = False
        print("You're right")
print ("\n")

#ex7

print("Type your favorite fruits plz (separate only with space)")
inpfruits = input("Type here: ")
favfruits = inpfruits.split(" ")
print("Good. Now write some fruit")
somefruit = input("Type some fruit here: ")
if somefruit in favfruits:
    print ("Good job")
else:
    print ("Bad job")
print ("\n")

# ex8

toppings = []
while True:
    print("\nHello sir what toppings are u want to ur pizza?")
    topping = input("Halo I want ")
    if topping == "stop":
        topprice = len(toppings)*10
        price = 300+ topprice
        print("Fine. You pay 300 bucks plus toppings so it is " + str(price) + ". The piza will be finished tomorrow.")
        break
    print("\nGod choice I added thats delishous " + topping + " to ur piza.")
    toppings.append(topping)
print ("\n")

# ex9

customerlist=[]
tickprice = 0
goodcustomer = True
print("\nHello its Cinema, type me (in numbers) all your ages separating with space ('' '') if u fails you don't go to watch movies")
ages = input("Halo my family ages is: ")
customerlist = ages.split(" ")
for i in range(0, len(customerlist)):
    if customerlist[i].isnumeric() == False:
        print("You can't read? I asked for numbers only, separated with space. Bye. Next please.")
        goodcustomer = False
        break
    if float(customerlist[i]) <= 3:
        print ("You have a baby. Little babies are not allowed because of crying. Next please.")
        goodcustomer = False
        break
    if (float(customerlist[i]) > 3) and (float(customerlist[i]) < 12):
        tickprice += 10
    else:
        tickprice += 15
if goodcustomer == True:
    print ("Fine. You have to pay " + str(tickprice) + "$.")
print ("\n")
    

#adults only film

from time import sleep
custnames = []
custages = {}
print("\nOk chaps, give me your names and we will decide can you enter to watch this tempting film.")
sleep(1)
while True:
    print("\nWhat is your name mate?")
    custname = input("Hi my name is ")
    if custname == "stop":
        break
    custnames.append(custname)
sleep(1)
print("\nOk, now I'll ask you for your age. Show me your passports.")
while True:
    for i in range(len(custnames)):
        print("\n" + custnames[i] + ", what is your age?")
        custage = input("Here, in my passport written that I am ")
        if custage.isnumeric():
            if float(custage) >= 18:
                custages[custnames[i]] = custage
    break
sleep(1)
if len(custages)==0:
    print("\nWhat I see? Either people are not able to clearly communicate their age, or they are under 18. Get out.")
else:
    print ("\nOk, so only " + ', '.join(list(custages)) + " are allowed to go in.")
print ("\n")


# ex10

sandwich_orders = ["Tuna sandwich", "Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Egg sandwich"]
saoptions = {}
for i in range(len(sandwich_orders)):
    if sandwich_orders[i] in saoptions:
        sandwich_orders[i] = "Another (position "+str(i)+") "+sandwich_orders[i]
    saoptions[sandwich_orders[i]] = i
print("\nOk, you are kitchen worker. The customer is waiting for his order! Make sandwitches quickly and say me which of them already finished!")
maxoption = max((saoptions.values()))
while len(saoptions) != 0:
    print("\nChoose the sandwitch you just made: " + str(saoptions))
    samade = input("Yea, just did the position number ")
    if samade.isnumeric() == False:
        print ("\nWhat is this rubbish? I asked you for number!")
        continue
    if int(samade) > maxoption:
        print("\nInattentive worker, this option does not exist!")
        continue
    try:
        readysandwich = list(saoptions.keys())[list(saoptions.values()).index(int(samade))] #gives the number of sandwitch muhan
    except ValueError:
        print("\nInattentive worker, you already made that sandwich!")
        continue
    print("\nFine. Work faster!")
    del saoptions[readysandwich] #removes sandwitch muhan from options to cook
print("\nOrder is ready!")
print("\nGood work!\n")
print ("\n")


# ex11

# No need