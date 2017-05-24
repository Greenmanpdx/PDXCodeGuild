import random

dice = input('What side dice are you rolling? ')
number = input('How many are you rolling? ')

print('You rolled ' + number + 'd' + dice + ' and got: ')

for i in range(1, int(number) + 1):
    print(random.randrange(1, int(dice) + 1))
