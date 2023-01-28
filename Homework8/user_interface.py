from teacher import give_mark

def menu():
    print('Кто пользуется программой?\n1 - учитель\n2 - ученик\n3 - Выход')
    print()
    choice = int(input('Выбор: '))
    return choice


def journal():
    flag = True
    give_mark()
    while(flag):
        print('Хотите выставить еще оценки?\n1 - да\n2 - нет')
        n = int(input('Выбор: '))
        if n == 1:
            give_mark()
        else:
            print()
            flag = False

