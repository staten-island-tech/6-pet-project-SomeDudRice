
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
# print(john.__dict__)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")
# John = BankAccount("john doe","9999999999$")
# print (John.__dict__)

class Pet:
    def __init__(self, name, happiness,hunger):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
    def play(self):
        self.__happiness +=10
        print (self.name, 'is playing fetch')
    def feed(self):
       self.hunger +=10
       print (self.name, 'is eating toddlers')
    def showstatus(self):
        print(self.name,"'s happiness is now",self.__happiness,"and fullness level is",self.hunger)
Armageddon = Pet("Armageddon senior",0,0)
isput = input()
choice = isput.capitalize()
end = 0
while end == 0:
    if choice == "Play":
     Armageddon.play()
    elif choice == "Show":
     Armageddon.showstatus()
    elif choice == "Feed":
       Armageddon.feed()
    elif choice == "End":
       End = 1
       print ("thanks for nurturing the messiah")
    else:
       print ("restart, no option exists")






