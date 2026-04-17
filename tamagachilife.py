
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = [inventory]
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
john = Hero("john doe",20,["barsoap"])
john.buy({"title": "Sword", "atk": 34})
print(john)


