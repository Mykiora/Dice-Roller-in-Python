from random import randint
from os import system


class Dice:
    def __init__(self, faces, quantity):
        self.faces = faces
        self.quantity = quantity

    def roll(self):
        roll_again = "R"
        while roll_again.upper() == "R":
            system("cls")
            if self.quantity == 1:
                roll_value = str(randint(1, self.faces))
                print("\n 1D" + str(self.faces) + "\nYou rolled a " + roll_value + "\n")
            else:
                print(" " + str(self.quantity) + "D" + str(self.faces))
                roll_values = tuple((str(randint(1, self.faces)) for i in range(0, self.quantity)))
                total_score = str(sum((int(roll_values[i]) for i in range(0, len(roll_values)))))
                print("Rolls results : " + ", ".join(roll_values) + "\nTotal : " + total_score + "\n")
            roll_again = input("Enter 'R' to roll again or anything else if you want to change dice => ")

    def ask_number_of_faces(self):
        print("How many faces do you want for your dice ? (classic is 6)")
        number_of_faces = self.verify_int()
        self.faces = number_of_faces

    def ask_dice_quantity(self):
        print("How many dices do you want to roll ?")
        quantity = self.verify_int()
        self.quantity = quantity

    def verify_int(self):
        try:
            number_str = input("=> ")
            number_int = int(number_str)
        except ValueError:
            print("Your input is not a number")
            return self.verify_int()
        else:
            return number_int


dice = Dice(0, 0)

while True:
    system("cls")
    dice.ask_number_of_faces()
    dice.ask_dice_quantity()
    dice.roll()
