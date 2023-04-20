    # @classmethod
    # def save():
    #     # inp = input('Type dish, price: ')
    #     inp = "Burger, 55"
    #     tuppl= tuple(inp.split(',') for inp in inp.split(';'))
    #     menu_db[tuppl[0][0]] = int(tuppl[0][1].strip())
    
    # @classmethod
    # def delete():
    #     inp = "Burger"
    #     # inp = input('Type the dish you want to delete: ')
    #     del menu_db[inp]
    
    # @classmethod
    # def update():
    #     MenuItem.save()
    
    # @classmethod
    # def all():
    #     return (menu_db)

menu_db = {'Angus': 9, 'Fish':12, "Apple":5}


class MenuItem:

    def __init__(self, dish, price):
        self.dish = dish
        self.price = price

    def save(self):
        menu_db[self.dish] = self.price

    def delete(self):
        del menu_db[self.dish]

    def update(self):
        MenuItem.save(self)

    @classmethod
    def all(cls):
        return menu_db
    
    @classmethod
    def get_by_name(cls,name):
        return next((MenuItem(name, price) for name, price in menu_db.items() if name == name), None)
    

    def get_by_name(self,name):
        return next((MenuItem(name, price) for name, price in menu_db.items() if name == self.dish), None)



print(MenuItem.get_by_name('Apple'))

# MenuItem.update()
# print(MenuItem.all())

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update()
# print(MenuItem.all())
