import math
from time import sleep

class CoffeeMachine():

    def __init__(self,milk: int,water:int ,coffee:int ) -> None:
        """Initialize coffee machine with milk, water and coffee amount"""
        self.milk = milk
        self.water = water
        self.coffee = coffee
        self.profit = 0

        print(f"I prepare espress, capuccino and latte from {self.milk},{self.coffee} and {self.water}")
    
    def prepare_latte():
        pass

    def accept_coins(self,amount):
        user_input = float(0)
        inputing_coin = True
        while inputing_coin:
            coin = input("Please insert coins: ")
            if coin == "nickel":
                user_input = math.fsum([user_input, 0.5])
            elif coin == "quarter":
                user_input = math.fsum([user_input,0.25]) 
            elif coin == "dimes":
                user_input = math.fsum([user_input,0.05])
            elif coin == "dollar":
                user_input = math.fsum([user_input,1.0])
            elif coin == "done":
                if user_input >= amount:
                    self.__return_exchange(user_input-amount)
                    return True
                else:
                    print("Insufficient amount. You don't get coffee!")
                    self.__return_exchange(user_input)
                    return False
    def add_profit(self,amount):
        print(f"Adding profit of {amount}$")
        self.profit = math.fsum([self.profit,amount])

    def prepare_cappucino(self):
        self.milk -= 150
        self.coffee -= 50
        self.water -= 50

        for i in range(10):
            print("..",end="",flush=True)
            sleep(1)
        print("\nYour Cappucino is ready, enjoy!")
        return True
    
    def prepare_latte(self):
        self.milk -= 200
        self.coffee -= 30
        self.water -= 50

        for i in range(10):
            print("..",end="",flush=True)
            sleep(1)
        print("\nYour Latte is ready, enjoy!")
        return True
    
    def prepare_espresso(self):
        self.water -= 50
        self.coffee -= 30
        for i in range(5):
            print("..",end="",flush=True)
            sleep(1)
        print("\nYour espresso is ready, enjoy!")
        return True
    
    def check_avaiable_materials(self,water=0,milk=0,coffee=0):
        is_available = True
        if self.water < water:
            is_available = False
            print("Sorry, not enough water in machine")
            return is_available
        if self.coffee < coffee:
            is_available = False
            print("Sorry, not enough coffee in machine")
            return is_available
        if self.milk < milk:
            is_available = False
            print("Sorry, not enough milk in machine")
            return is_available
        return is_available

    def report(self):
        print(f"Current situation is:\nMilk: {self.milk}\nCoffee: {self.coffee}\nWater: {self.water}\nProfit: {self.profit}$")

    @staticmethod
    def __return_exchange(amount):
        if amount == 0.0:
            return
        print(f"Please take your change of {amount}$")
            
    def operate(self):
        operating_condition = True

        while operating_condition:
            user_choice = input("What would you like? ")
            if user_choice == "off-operator": 
                print("Coffee Machine going to sleep")
                operating_condition = False

            elif user_choice == "latte":
                if self.check_avaiable_materials(water=50,milk=200,coffee=30):
                    if self.accept_coins(2.5):
                        print("preparing latte:")
                        self.prepare_latte()
                        self.add_profit(2.5)
                else:
                    print("Choose something else")
            elif user_choice == "cappucino":
                if self.check_avaiable_materials(water=50,milk=150,coffee=50):
                    if self.accept_coins(3.0):
                        print("Preparing cappucino")
                        self.prepare_cappucino()
                        self.add_profit(3.0)
                else :
                    print("Choose something else")
            elif user_choice == "espresso":
                if self.check_avaiable_materials(water=30,coffee=50):
                    if self.accept_coins(1.5):
                        print("Preparing espresso")
                        self.prepare_espresso()
                        self.add_profit(1.5)
                else :
                    print("Choose something else")
            elif user_choice == "report":
                self.report()
                continue
            else:
                print("Non existing option")
                continue

if __name__ == "__main__":
    milk_amount,water_amount,coffee_amount = [int(input(f"Please insert amount of {material}: ")) for material in ["milk","water","coffee"]]
    coffee_machine1 = CoffeeMachine(milk=milk_amount,water=water_amount,coffee=coffee_amount)
    coffee_machine1.operate()