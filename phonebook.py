import csv
class contact:

    def __init__(self, name, phone, phrase):
        self.name = name
        self.phone = phone
        self.phrase =phrase


def open_phonebook():
    contact_list = []
    with open('phonebook.txt', 'r+') as book:
        read_data = csv.reader(book, delimiter =',', )
        for row in read_data:
            contact_list.append(contact(row[0], row[1], row[2]))

    return contact_list




def view_phonebook(contact_list):
    print(contact_list)


def add_contact_menu(contact_list):
    name = intput('Enter the name: ')
    number = input('Enter the phone #: ')
    phrase = input('Enter the catchphrase: ')
    contact_list.append(contact(name, number, phrase))

def search_name(contact_list):
    name_wanted = input('Enter name to search: ')
    name_list = [x for x in contact_list if x.name == name_wanted]

def search_phrase(contact_list):

def search_contact_menu(contact_list):
    running = True
    while running == True:
        query = input('1. search by name \n'
                      '2. search by phrase \n'
                      'b. Go back \n')

        if query == '1':
            search_name(contact_list)
        if query == '2':
            search_phrase(contact_list)
        if query == 'b':
            running == False
        else:
            print('invalid entry')

contact_list = open_phonebook()
running = True

try:
    query = input('Phonebook main menu \n'
                  '1. View Phonebook \n'
                  '2. Add contact \n'
                  '3. Edit contact \n'
                  '4. Search contacts \n'
                  'q. quit \n')
    if query == '1':
        view_phonebook(contact_list)
    if query == '2':
        add_contact_menu(contact_list)
    if query == '3':
        search_contact_menu(contact_list)
    if query == 'q':
        break
    else:
        print('invalid entry, please try again')

except:
    print('invalid entry, please try again')