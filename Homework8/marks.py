
subjects = ['Математика', 'Русский', 'Литература', 'Музыка', 'История']

def open_files():
    subjects = ['Математика', 'Русский', 'Литература', 'Музыка', 'История']
    for s in subjects:
        f = open(f'Homework8/{s}.txt', 'a')