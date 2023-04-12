
# Exercises XP+

# ex1
class Family:
    def __init__(self, members, surname):
        self.members = members
        self.surname = surname

    def new(self, newmember):
        nm = {}
        nm["name"] = newmember[0]
        nm["age"] = newmember[1]
        nm["gender"] = newmember[2]
        if nm["age"]<18: nm["is_child"] = True 
        else:            nm["is_child"] = False
        self.members.append(nm)
        return nm

    def __repr__(self):
        from copy import deepcopy
        rep=""
        a = deepcopy(self.members)
        for j in a:
            j['name']+=f" {self.surname}"
            rep+=("\n" + "\n".join("{!r}: {!r}".format(k, v) for k, v in j.items()) + "\n") 
        return ''.join(l for l in rep if l!="'")
    
    def family_presentation(self):
        guys = lambda people: ', '.join([person['name'] for person in people[:-1]]) + f" and {people[-1]['name']}"
        print(f"Here they are from left to right: {guys(self.members)} {self.surname}s")
    

fam = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Johnson")


fam.new(["Pasha", 12, "not_decided_yet"])
print(fam)
print (fam.family_presentation())


# ex2

class TheIncredibles(Family):
    def __init__(self, members, surname):
        super().__init__(members, surname)

    def new(self, newmember):
        new_member = super().new(newmember)
        new_member["power"] = newmember[3]
        new_member["incredible_name"] = newmember[4]
        return new_member

    def use_power(self, manname):
        man = (lambda name: next((person for person in self.members if person['name'] == name), None))
        if man(manname)['age']>=18:
            person = f"{man(manname)['name']} have superpower: to {man(manname)['power']}"
            print(person)
        else: raise Exception ("This guy is too young for these things")

    def incredible_presentation(self):
        super().family_presentation()



superfam = TheIncredibles([
    {'name':'Cock','age':55,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Chook','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}], "Dunder")

superfam.new(["Pasha", 12, "not_decided_yet", "Sleep", "LazyPasha"])
print(superfam)
superfam.incredible_presentation()





########## Not related to homework ############


# class Animal:
#     def __init__(self, name: str):
#         self.name = name

#     def breathing(self):
#         out = f'{self.name} breaths'
#         print(out)


# class Mammal(Animal):
#     def produce_milk(self):
#         print(f'{self.name} produces milk')


# class SeaMammal(Mammal):
#     def hold_breath (self):
#         print(f'{self.name} holding breath')        



# mammal = SeaMammal(name="dolph")
# mammal.hold_breath()



# def iphone_block(password = 1234):
#     import time

#     user_pass=None
#     tries = 0
#     blocktime=0
#     tri=[3,4,5,8,10,12,15,20,25,30]

#     def sleep(num):
#         for i in range(num):
#             print("\rTime remaining: {} seconds.".format(num - i), end='')
#             time.sleep(1)
#         print("\n")

#     while user_pass!=password:
#         try:
#             user_pass = int(input("password: "))
#             if user_pass != password:
#                 print("wrong password")
#                 tries+=1
#             else:
#                 print("You passed.")
#             if tries==tri[0]:
#                 del tri[0]
#                 blocktime=round((blocktime**1.5)+1)
#                 print(f"tries has blocked for {blocktime} sec")
#                 sleep(blocktime)
#         except ValueError:
#             print("not a number")
#             continue

# iphone_block(password=1)


