def check(word):
    backwards = word[::-1]
    if word == backwards:
        return True
    else:
        return False


word = input('Is your word a palindrome? Enter your word: ')

lst = [x for x in word]

for i in range(0, len(lst)):
    if lst[i].isalpha() != True:
        del lst[i]
word = ''.join(lst)

if check(word) == True:
    print('Yes ' + word + ' is a palindrome')
else:
    print('No ' + word + ' is not a palindrome')

