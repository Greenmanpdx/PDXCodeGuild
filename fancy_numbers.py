phone = input('Enter a phone number with all numbers')

num_lst = [x for x in phone]

num_lst.insert(3, '-')
num_lst.insert(7, '-')
phone = ''.join(num_lst)

print(phone)
