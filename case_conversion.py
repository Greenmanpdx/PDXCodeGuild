def case_type(lst):
    for x in lst:
        if x.isupper():
            return 'camel'
        if x == '_':
            return 'snake'

# def to_snake(lst):
#     for x in lst:
#         if x.isupper():
#             lst[x].tolower()
#             lst.insert(x, '_')
#
# def to_camel(lst):
#     # i = lst.count("_")
#     # for a in range(0, i):
#         x = lst.index("_")
#         list.remove("_")
        # lst.toupper(x)

    # for x in lst:
    #      if x == '_':
    #          list.remove("_")
    #          x.toupper()

word = input('Enter a word in either snake or camel case:  ')
lst = [x for x in word]

case = case_type(lst)

# if case == 'camel':
#     to_snake(lst)
#
# if case == 'snake':
#     to_camel(lst)
#
# final_word = ''.join(lst)

print('Your converted word is in ' + case + ' case')
