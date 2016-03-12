from random import randint

class DiceRoller:
    def __init__(self, rolls, sides, dice):
        self.rolls = rolls
        self.sides = sides
        self.dice = dice
​
    def die_roll(self):
        random_num = randint(1, self.sides)
        return random_num
​
    def roll_dice(self):
        outcome = []
        for i in range(0, self.rolls):
            outcome.append(self.die_roll())
        print(outcome)
​
how_many_dice = int(input("How many dice should we roll?"))
how_many_sides = int(input("How many sides should the dice have?"))
​
my_roller = DiceRoller(5, how_many_sides, how_many_dice)
my_roller.roll_dice()
