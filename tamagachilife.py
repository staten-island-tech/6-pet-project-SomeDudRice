
# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = [inventory]
#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)
# john = Hero("john doe",20,{"title":"barsoap", "atk" : 999})
# john.buy({"title": "Sword", "atk": 34})
# print(john.__dict__)\

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
John = BankAccount("john doe","9999999999$")
print (John.__dict__)
Jane = BankAccount("jane doe","0.000000000000000000-000-0-0000001$")
print (Jane.__dict__)



