time = input('What time is it? (ex. 7am) ')

lst = [x for x in time]

numbers = [x for x in lst if x.isdigit()]
letter = [x for x in  lst if x.isalpha()]
time = int(''.join(numbers))


if letter[0] == 'a':
    if 6 < time <= 9:
        meal = 'Breakfast'
    if time <= 4 or time == 12:
        meal = 'Hammer'

if letter[0] == 'p':
    if time == 12 or time <=2:
        meal = 'Lunch'
    elif 7 <= time <= 9:
        meal = 'Dinner'
    elif time >= 10:
        meal = 'Hammer'

answer = "You should be eatiing " + meal


print(answer)
