import math

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def count_words(file):
    num_words = 0
    for word in file.read().split():
        num_words += 1

    return num_words

def count_characters(file):
    file.seek(0)
    number_chars = 0
    blanks = 0
    for line in file:
        number_chars += len(line)
        for char in line:
            if char == ' ' or char == '\n':
                blanks += 1

    return number_chars - blanks


def count_sentences(file):
    file.seek(0)
    count = 0
    for line in file:
        for c in line:
            if c == '.' or c == '!' or c == '?':
                count += 1
    return count


def open_file(text):
    return open(text, 'r', encoding="utf-8-sig")
    # print(type(text))


def calculate_score(x,y,z):
    return 4.71 * x  / y + 0.5 * y  /z - 21.43

book_dict = {
                1: 'geneology_of_morals.txt',
                2: 'gettysburg_address.txt',
                3: 'jack_and_jill.txt',
                4: 'iliad.txt',
                5: 'marketing_ipsum.txt',
                6: 'odyssey.txt',
                7: 'po.txt',
                8: 'the_room_with_the_little_door.txt'
}
query = 0
while query != 'q':
    query = input('To compute its automated readability index,\n'
                    'pick from one of the files below: \n'
    
                    '1) geneology-of-morals.txt \n' 
                    '2) gettysburg-address.txt \n'
                    '3) jack-and-jill.txt \n'
                    '4) iliad.txt \n'
                    '5) marketing_ipsum.txt \n'
                    '6) odyssey.txt \n'
                    '7) po.txt \n'
                    '8) the_room_with_the_little_door.txt \n'
    
                    'or \n'
    
                    'q) Quit \n')

    if query == 'q':
        break
    else:
        file = open_file(book_dict[int(query)])

        b = count_words(file)
        a = count_characters(file)
        c = count_sentences(file)
        score = math.ceil(calculate_score(a,b,c))
        if score > 14:
            look_up = 14
        else:
            look_up = score
        print('The ARI for ' + book_dict[int(query)] + ' is ' + str(score))
        print('This coresponds to a(n) ' + ari_scale[look_up]['grade_level'] + ' level of difficulty' )
        print('that is suitible for an average person ' + ari_scale[look_up]['ages'] + ' years old \n')
        print('character: ' + str(a))
        print('words: ' + str(b))
        print('sentences:' + str(c))