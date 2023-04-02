# ex1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

kot = Cat("Kot", 299)
kit = Cat("Kit", 3)
kat = Cat("Kat", 22)

def oldcat(catlist):
    youngest = sorted(catlist, key=lambda cat: cat.age, reverse=True)
    
    print((youngest[0]).age)
    return()

catlist = [kot, kit, kat]
oldcat(catlist)

# ex2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(self.name +  " goes woof!")

    def jump(self):
        jump = self.height*2
        print(f"{self.name} jumps {jump} cm high!")



sobaka = Dog("Sobaka", 80)
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

Dog.jump(davids_dog)
Dog.jump(sarahs_dog)

if (davids_dog.height)>(sarahs_dog.height):
    print (davids_dog.height)
else:
    print(sarahs_dog.height)


# ex3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for x in self.lyrics:
            print (x)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])  
Song.sing(stairway)

# ex4
class Zoo:
    def __init__(self, zooname):
        self.zooname = zooname
        self.animals = ["Zz", "Ape","Baboon","Omg", "Bear",'Cat', 'Cougar','Eel', 'Emu']

    def add_animal(self, newanimal):
        if not newanimal in self.animals:
            self.animals.append(newanimal.capitalize())

    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)

    def sort_animals(self):
        lista = sorted(self.animals)
        animaldict = {}
        cou=1
        iterable=[]
        for i in range(len(lista)):
            if not cou in animaldict:
                animaldict[cou]=iterable

            iterable.append(lista[i])
            animaldict[cou]=iterable
            if i!=(len(lista)-1):
                if lista[i][0]!=lista[i+1][0]:
                    cou+=1
                    iterable=[]
        return (animaldict)

# def sort_animal(self):
#         sorted_animals = sorted(self.animals)
#         grouped_animals = {}

#         for animal in sorted_animals:
#             if (not grouped_animals):
#                 grouped_animals[1] = [animal]
#             else:
#                 if (animal[0] == grouped_animals[len(grouped_animals)][0][0]):
#                     grouped_animals[len(grouped_animals)].append(animal)
#                 else:
#                     grouped_animals[len(grouped_animals)+1] = [animal]

#         return grouped_animals



m = Zoo("ramat_gan_safari")
m.add_animal("arg")
print(m.sort_animals())
m.sell_animal("Bear")
m.get_animals()

# daily challenge

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {"Bear":1,'Cat':1, 'Cougar':1}

    def add_animal(self, animal, *args):
        if args:
            amount = args[0]
        else:
            amount=1
        if not animal in self.animals:
            self.animals[animal]=amount
        else:
            self.animals[animal]+=amount            

    def get_info(self):
        a = "\n".join(list(map(lambda x,y: str(x)+" : "+str(y), self.animals, self.animals.values())))
        return(f"McDonald's farm\n\n{a}\n\n\tE-I-E-I-0!")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())