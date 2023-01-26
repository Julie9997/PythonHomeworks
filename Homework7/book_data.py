import csv

def new_contact():
    contact = []
    lastname = input('Введите фамилию: ')
    contact.append(lastname)
    firstname = input('Ведите имя: ')
    contact.append(firstname)
    phone = input('Введите телефон: ')
    contact.append(phone)
    description = input('Введите описание: ')
    print()
    contact.append(description)
    return contact

def show_book(view):
    if view == 1:
        with open('homework7/phone_book1.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end=' ')
            print()
    if view == 2:
        with open('homework7/phone_book2.txt', 'r', encoding='utf-8')as file:
            for line in file:
                print(line, end='\n')

def save_data(contact):
    with open('homework7/phone_book1.txt', 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {contact[0]}\nИмя: {contact[1]}\nТелефон: {contact[2]}\nОписание: {contact[3]}\n')
        file.write('-----------------------------------\n')
    with open('homework7/phone_book2.txt', 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Описание: {contact[3]}\n')

