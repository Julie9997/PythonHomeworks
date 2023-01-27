from user_interface import menu, journal
from student import see_marks

def control():
    while True:
        selection = menu()
        if selection == 1:
            journal()
        elif selection == 2:
            see_marks()
        elif selection == 3:
            break