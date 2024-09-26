import random

for i in range(3):
    print(random.random())


# Random values between 10 and 20
for i in range(3):
    print(random.randint(10,20))


# Randomly picking an item from a list
members = ['John', 'Mary', 'Bob', 'Jack', 'Daniel']
leader = random.choice(members)
print(leader)

# Exercise: to roll a dice
class Dice:
    def roll(self):
        # tuple = (0, 0)
        first_number = random.randint(1,6)
        second_number = random.randint(1,6)
        return first_number, second_number


dice = Dice()
print(dice.roll())

