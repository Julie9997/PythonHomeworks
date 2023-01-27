import marks as m

def get_mark():
    mark = input('Введите оценку: ')
    return mark

def give_mark():
    sub = input('Введите название предмета: ')
    sub = sub.capitalize()
    if sub in m.subjects:
        lastname = input('Введите фамилию учащегося: ')
        mark = get_mark()
        if in_file(sub, lastname):
            with open(f'{sub}.txt',  'r', encoding='utf-8') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                if lastname in lines[i]:
                    lines[i] = lines[i].replace('\n', ' ') + mark + '\n'
            with open(f'{sub}.txt', 'w', encoding='utf-8') as file:
                file.writelines(lines)
        else:
            with open(f'{sub}.txt',  'a', encoding='utf-8') as file:
                file.write(f'{lastname} {mark}\n')
    else:
        print('Ошибка! Такого предмета нет.')

def in_file(subject, lastname):
    with open(f'{subject}.txt',  'r', encoding='utf-8') as file:
        if lastname in file.read():
            return True
        else:
            return False
