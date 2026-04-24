
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
inname = input("what do you want to name your pet?")
class Pet:
    def __init__(self, name, happiness,hunger,energy):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
        self.energy = energy
    def play(self):
        self.__happiness +=10
        print (self.name, 'is playing fetch')
        print (self.name, "'s happiness is now",self.__happiness)
    def feed(self):
       self.hunger +=10
       print (self.name, "'s fullness is now",self.hunger)
       print (self.name, 'is eating toddlers')
    def rest(self):
       self.energy +=10
       print (self.name, "'s energy is now",self.energy)
       print (self.name, 'is now eepy *silly gubby humor core >w<*')
    def showstatus(self):
        print(self.name,"'s happiness is now",self.__happiness,"and fullness level is",self.hunger)
Armageddon = Pet(inname,0,0,0)
isput = input("enter play, feed, or nap to preform actions and show to show stats,")
choice = isput.capitalize()
end = 0
while end == 0:
 if choice == "Play":
      Armageddon.play()
 elif choice == "Show":
      Armageddon.showstatus()
 elif choice == "Feed":
      Armageddon.feed()
 elif choice == "Nap":
      Armageddon.rest()
 elif choice == "End":
      end = 1
      print (inname,"has been shipped to the glue factory ")
 else:
     print("please repeat it")
 if end == 0:
      isput = input("enter play, feed, or nap to preform actions and show to show stats,")
      choice = isput.capitalize()
print ("thanks for playinmg")






