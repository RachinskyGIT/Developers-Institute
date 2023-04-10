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



def iphone_block(password = 1234):
    import time

    user_pass=None
    tries = 0
    blocktime=0
    tri=[3,4,5,8,10,12,15,20,25,30]

    def sleep(num):
        for i in range(num):
            print("\rTime remaining: {} seconds.".format(num - i), end='')
            time.sleep(1)
        print("\n")

    while user_pass!=password:
        try:
            user_pass = int(input("password: "))
            if user_pass != password:
                print("wrong password")
                tries+=1
            else:
                print("You passed.")
            if tries==tri[0]:
                del tri[0]
                blocktime=round((blocktime**1.5)+1)
                print(f"tries has blocked for {blocktime} sec")
                sleep(blocktime)
        except ValueError:
            print("not a number")
            continue

iphone_block(password=1)