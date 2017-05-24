import random

answer = random.randrange(1, 2 * 10 ** 9 )

def check_number(guess):
    if guess == answer:
        return 'winner'
    if guess > answer:
        return "lower"
    if guess < answer:
        return "higher"

print('Hello and welcome to the guessing game. \n')
winning = 'no'
score = 0
while winning != 'winner':
    guess = int(input('Enter your guess: '))
    score += 1
    winning = check_number(guess)
    print(winning)

print('Your score is ' + str(score))

