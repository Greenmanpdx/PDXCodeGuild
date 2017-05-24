my_list = [x for x in range(0, 101)]

for i in range(0, 101):
    if (my_list[i] % 3 == 0) and (my_list[i] % 5 == 0):
        my_list[i] = 'fizzbuzz'
    elif my_list[i] % 3 == 0:
        my_list[i] = 'fizz'
    elif my_list[i] % 5 == 0:
        my_list[i] = 'buzz'

print(my_list)
