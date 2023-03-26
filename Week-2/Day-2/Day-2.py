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

# 1. The difference is so, that float is not integer, and integer is not float
# 2. from random import random \ seq=[] \ for i in range(0, 999): seq.append(random()) \ PROFIT!
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
