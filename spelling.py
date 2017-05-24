excepts = ['weird', 'weigh', 'neighbor', 'veil', 'atheism']
def spell_test(word):
    if word in excepts:
        return True
    for x in range(0, len(word) + 1):
        if word[x] == 'i':
            if word[x + 1] == 'e':
                return True
        elif word[x] == 'e':
            if word[x + 1] == 'i':
                return False




word = input('enter a word with an ie or ei in it: ')
rule = spell_test(word)

if rule == True:
    print("The rule has been followed")
else:
    print("You broke the rules")