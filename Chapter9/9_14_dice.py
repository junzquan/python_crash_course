import random

class Dice():
    def __init__(self, sided):
        self.sides = 6
        self.sided = sided

    def roll_dice(self):
        self.sides = random.randint(1, self.sided)
        print("Roll a " + str(self.sided) + " sided dice: " + str(self.sides))


six_sided_dice = Dice(6)
for i in range(0, 10):
    six_sided_dice.roll_dice()

ten_sided_dice = Dice(10)
for i in range(0, 10):
    ten_sided_dice.roll_dice()

tw_sided_dice = Dice(20)
for i in range(0, 10):
    tw_sided_dice.roll_dice()
    