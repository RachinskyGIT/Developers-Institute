# exc8

print("insert your number ")
num=input()
num = float(num)

if (num%2)==0:
    print ("true number")
else: 
    print ("wrong number you lost")


# exc9

print("insert your name ")
input = input()
if input == "A":
    print ("good name ")
else:
    print ("bad name ")


# ---------------------
# gold and ninja excersices


# ex1

print ("Hello w "*5 + "I love "*5)

# ex2

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
           Ut enim ad minim veniam, quis nostrud exercitation ullamco \
           laboris nisi ut aliquip ex ea commodo consequat. \
           Duis aute irure dolor in reprehenderit in voluptate velit \
           esse cillum dolore eu fugiat nulla pariatur. \
           Excepteur sint occaecat cupidatat non proident, \
           sunt in culpa qui officia deserunt mollit anim id est laborum."

print (len(my_text))

# ex5

while True:
    print("\nI'am sking you to input the longest sentence you can without the character “A”.")
    inp = str(input("Type here: ")).lower()
    if inp == "plz stop master!":
        print ("\nok bye")
        break
    if "a" in inp:
        print ("\nyou loose looser!")
        break
    cou = (len(inp))
    try:
        if (cou <= cou1):
            print ("\nyou are a lazy dog. goodbye.")
            break
    except NameError:
        cou1=0
    cou1 = (len(inp))
    print ("\nCongrats! Go on!\n")


# Daily challenge
from random import random


print("You asked for a string. The string must be 10 characters long.")
inputdaily = input("Type here: ")
if len(inputdaily) !=((random()*10)**2//2):
    print ("loser")
else:
    print ("looser at any case")

print("First and last characters of the given text: " + inputdaily[0] + " and " + inputdaily[-1])

for i in range(len(inputdaily)):
    print(inputdaily[:i+1])