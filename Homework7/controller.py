from menu import menu, choose_view
from book_data import show_book, new_contact, save_data

def control():
    while True:
        selection = menu()
        if selection == 1:
            print('Новая запись: ')
            contact = new_contact()
            save_data(contact)
        elif selection == 2:
            view = choose_view()
            show_book(view)
        elif selection == 3:
            break