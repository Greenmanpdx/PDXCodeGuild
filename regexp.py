import re

def scrub_numbers(word):
    clean_word = re.sub(r'[0-9]', '', word)
    print(clean_word)

scrub_numbers('Be9autiful19 i4s be2tter th4an ug42ly')

def gentle_clean(word):
    print(re.sub(r'[-_]', ' ', word))

gentle_clean('Explicit_is-better_than -implicit')

def clean_data(word):
    word1 = re.sub(r'\s', '' , word)
    word2 = re.sub(r'[0-9]', '', word1)
    word3 = re.sub(r'[-_]', ' ', word2)
    # word4 = re.findall(r'\w+', word3)
    print(word3)

clean_data('  42Simple-is_better_than-compl9ex   ')

def some_scrubber(word):
    word = re.sub(r'(\w)(\s)', r'\1', word)
    print(re.sub(r'\s\s', ' ', word))

some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')


def mr_clean(word):
    print(re.sub(r'(\w)', r' \1', word))

mr_clean('Sparse is better than dense')

def ms_clean(sentence):

    word_list = sentence.split()
    new_sentence = []
    for word in word_list:
        number = len(word)-2
        char_list = list(word)
        del char_list[1:-1]
        char_list.insert(1, str(number))
        new_word = ''.join(char_list)
        new_sentence.append(new_word)
    final_word = ' '.join(new_sentence)
    print(final_word)
    # word3 = re.sub(r'(\w)(\w*)(\w)', r'\1\3', word)
    # print(list(word))

ms_clean('Readability counts')

def strong_cleaner(word):
    print(re.sub(r'[@#$%&*!()1I]', '', word))

strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')


def extracto(word):
    print(re.sub(r"^'|'$|\d", '', word))

extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.")
extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.")
extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.")

