import csv
class contact:

    def __init__(self, name, phone, phrase):
        self.name = name
        self.phone = phone
        self.phrase =phrase

    def __str__(self):
        return("Name: " + str(self.name)+ " Phone: " + str(self.phone) + " Catchphrase: " + str(self.phrase) + '\n')

    def __repr__(self):
        return str(self)

def open_phonebook():
    contact_list = {}
    i = 0
    with open('contacts.csv', 'r') as book:
        read_data = csv.reader(book, delimiter =',', )
        for row in read_data:
            i+=1
            contact_list[i] = (contact(row[0], row[1], row[2]))

    return contact_list

def close_phonebook(contact_list):
    with open('contacts.csv', 'w') as book:
        write_data = csv.writer(book, delimiter= ',', quotechar='|',
                               quoting=csv.QUOTE_NONE)
        for key, value in contact_list.items():
            # print(value)
             write_data.writerow([value.name, value.phone, value.phrase])


def view_phonebook(contact_list):
    print(contact_list)


def add_contact_menu(contact_list):
    name = input('Enter the name: ')
    number = input('Enter the phone #: ')
    phrase = input('Enter the catchphrase: ')
    contact_list.append(contact(name, number, phrase))

def search_name(contact_list):
    name_wanted = input('Enter name to search: ')

    name_list = {x for x in contact_list.items() if name_wanted in x[1].name}

    print(name_list)

def search_phrase(contact_list):
    phrase_wanted = input('Enter phrase to search: ')
    phrase_list = {x for x in contact_list if phrase_wanted in x[1].phrase}
    print(phrase_list)

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

def edit_contact(contact_list, key_to_edit):
    print(contact_list[int(key_to_edit)])
    selection = input('1. Edit name \n'
                      '2. Edit Number \n'
                      '3. Edit Phrase \n')
    if selection == '1':
        edit_name(contact_list, key_to_edit)
    if selection == '2':
        edit_number(contact_list, key_to_edit)
    if selection == '3':
        edit_phrase(contact_list, key_to_edit)

def edit_name(contact_list, key_to_edit):
    name = input('Enter new name: ')
    contact_list[int(key_to_edit)].name = name

def edit_number(contact_list, key_to_edit):
    number = input('Enter new number: ')
    contact_list[int(key_to_edit)].number = number

def edit_phrase(contact_list, key_to_edit):
    phrase = input('Enter new Phrase: ')
    contact_list[int(key_to_edit)].phrase = phrase


def edit_contact_menu(contact_list):
    view_phonebook(contact_list)
    selection = input('Select the number of the contact to edit: ')
    edit_contact(contact_list, selection)

def delete_contact_menu(contact_list):
    view_phonebook(contact_list)
    selection = input('Select the number of the contact to delete: ')
    del contact_list[int(selection)]


contact_list = open_phonebook()
running = True

while running == True:
    query = input('Phonebook main menu \n'
                  '1. View Phonebook \n'
                  '2. Add contact \n'
                  '3. Search contacts \n'
                  '4. Edit contact \n'
                  '5. Delete contact \n'
                  'q. quit \n')
    if query == '1':
        view_phonebook(contact_list)
    if query == '2':
        add_contact_menu(contact_list)
    if query == '3':
        search_contact_menu(contact_list)
    if query == '4':
        edit_contact_menu(contact_list)
    if query == '5':
        delete_contact_menu(contact_list)
    if query == 'q':
        close_phonebook(contact_list)
        break
    else:
        print('invalid entry, please try again')

